import pandas as pd
from sqlalchemy import create_engine
import os
import logging
import time
import gc

# Ensure log folder exists
os.makedirs("log", exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename="log/ingestion_db.log",
    filemode="a"
)

engine = create_engine("sqlite:///inventory.db")

def ingest_db(file_path, table_name, engine):
    """Ingest CSV in chunks to avoid memory issues"""
    
    for i, chunk in enumerate(pd.read_csv(file_path, chunksize=50000, low_memory=True)):
        chunk.to_sql(
            table_name,
            con=engine,
            if_exists='replace' if i == 0 else 'append',
            index=False
        )

def load_raw_data():
    """Load CSV files and ingest into DB"""
    
    start = time.time()

    for file in os.listdir('data'):
        if file.endswith('.csv') and 'checkpoint' not in file:
            try:
                file_path = os.path.join('data', file)
                
                logging.info(f'Ingesting {file} into DB')

                ingest_db(file_path, file[:-4], engine)

                gc.collect()  # 🔥 free memory after each file

            except Exception as e:
                logging.error(f'Error processing {file}: {e}')

    end = time.time()
    total_time = (end - start) / 60

    logging.info('--------------------Ingestion Completed--------------------------')
    logging.info(f'Total Time Taken: {total_time:.2f} minutes')

if __name__ == '__main__':
    load_raw_data()