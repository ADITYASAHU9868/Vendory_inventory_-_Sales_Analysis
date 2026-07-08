import pandas as pd
import logging
import time
import gc
from ingestion_db import ingest_db

# Ensure log folder exists
os.makedirs("log", exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename="get_vendor_summary.log",
    filemode="a"
)

def create_vendor_summary(conn):
    '''this function will merge the different tables to get the overall vendor summary and adding new columns in the resutant data'''
    vendor_sales_summary = pd.read_sql_query("""
    WITH FreightSummary AS (
        SELECT
            VendorNumber,
            SUM(Freight) AS FreightCost
        FROM vendor_invoice
        GROUP BY VendorNumber
    ),

    PurchaseSummary AS (
    SELECT
        p.VendorNumber,
        p.VendorName,
        p.Brand,
        p.Description,
        pp.Volume,
        pp.PurchasePrice,
        pp.Price AS ActualPrice,
        SUM(p.Quantity) AS TotalPurchaseQuantity,
        SUM(p.Dollars) AS TotalPurchaseDollars
    FROM purchases p
    JOIN purchase_prices pp
        ON p.Brand = pp.Brand
    GROUP BY
        p.VendorNumber,
        p.VendorName,
        p.Brand,
        p.Description,
        pp.Volume,
        pp.PurchasePrice,
        pp.Price
    ),
    
    SalesSummary AS (
    SELECT
        VendorNo,
        Brand,
        SUM(SalesQuantity) AS TotalSalesQuantity,
        SUM(SalesDollars) AS TotalSalesDollars,
        SUM(SalesPrice) AS TotalSalesPrice,
        SUM(ExciseTax) AS TotalExciseTax
    FROM sales
    GROUP BY VendorNo, Brand
    )
    
    SELECT
    p.VendorNumber,
    p.VendorName,
    p.Brand,
    p.Description,
    p.Volume,
    p.PurchasePrice,
    p.ActualPrice,
    
    p.TotalPurchaseQuantity,
    p.TotalPurchaseDollars,
    
    s.TotalSalesQuantity,
    s.TotalSalesDollars,
    s.TotalSalesPrice,
    s.TotalExciseTax,
    
    f.FreightCost
    
    FROM PurchaseSummary p
    
    LEFT JOIN SalesSummary s
    ON p.VendorNumber = s.VendorNo
    AND p.Brand = s.Brand
    
    LEFT JOIN FreightSummary f
    ON p.VendorNumber = f.VendorNumber
    
    ORDER BY p.TotalPurchaseDollars DESC
    """, conn)

    return vendor_sales_summary

def clean_data(df):
    '''this function will clean the data'''
    # change datatype to float
    df['Volume'] = df['Volume'].astype('float64')

    # filling missing value with 0
    df.fillna(0, inplace=True)

    # remove space in catagorical colums
    df['VendorName'] = df['VendorName'].str.strip()

    # create new columns for better analysis
    df['GrossProfit'] =  df['TotalSalesDollars'] - df['TotalPurchaseDollars']
    df['ProfitMargin'] =  (df['GrossProfit'] / df['TotalSalesDollars'])*100
    df['StockTurnover'] = df['TotalSalesQuantity'] / df['TotalPurchaseQuantity']
    df['SalestoPurchaseRatio'] = df['TotalSalesDollars'] / df['TotalPurchaseDollars']

    return df

if __name__ == '__main__':

    # creating database connection
    conn = sqlite3.connect('inventory.db')

    logging.info('Creating Vendor Summary Table.....')
    summary_df = create_vendor_summary(conn)
    logging.info(summary_df.head())

    logging.info('Cleaning Data.....')
    clean_df = clean_data(summary_df)
    logging.info(clean_df.head())

    logging.info('Ingesting data.....')
    ingest_db(clean_df, 'vendor_sales_summary', conn)

    logging.info('Process Completed')