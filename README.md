# Inventory & Vendor Performance Analytics

An end-to-end **Business Analytics** project that analyzes procurement, sales, pricing, inventory, and vendor performance using **Python, SQL, SQLite, Pandas, and Statistical Analysis**. This project transforms raw transactional data into actionable business insights that help optimize procurement strategies, improve inventory management, and support data-driven decision-making.

---

##  Project Overview

Efficient inventory and procurement management are essential for maximizing profitability and maintaining a resilient supply chain. This project integrates multiple business datasets into a unified analytical model and performs comprehensive exploratory data analysis, feature engineering, statistical testing, and business intelligence to uncover valuable insights.

The project demonstrates an end-to-end analytics workflow, including:

- Data Ingestion
- Data Cleaning & Validation
- SQL-Based Data Integration
- Feature Engineering
- Exploratory Data Analysis (EDA)
- Statistical Analysis
- Business Insights & Recommendations

---

#  Business Objectives

The primary objectives of this project are:

- Analyze vendor procurement performance.
- Evaluate sales and profitability across vendors and brands.
- Identify slow-moving inventory and excess stock.
- Estimate capital locked in unsold inventory.
- Study the impact of bulk purchasing on procurement cost.
- Detect high-profit but low-selling products.
- Perform statistical analysis on vendor profitability.
- Generate actionable business recommendations.

---

# 🗂 Dataset

The project integrates the following business datasets:

| Dataset | Description |
|----------|-------------|
| Purchases | Purchase transactions from vendors |
| Sales | Product sales transactions |
| Purchase Prices | Vendor purchase prices |
| Vendor Invoices | Freight and logistics costs |
| Beginning Inventory | Opening inventory |
| Ending Inventory | Closing inventory |

These datasets were consolidated into a single analytical table called **Vendor Sales Summary**.

---

# 🛠 Tech Stack

### Programming

- Python
- SQL

### Database

- SQLite
- SQLAlchemy

### Libraries

- Pandas
- NumPy
- Matplotlib
- Seaborn
- SciPy

### Development Environment

- Jupyter Notebook

---

# ⚙ Project Workflow

## 1️⃣ Data Ingestion

- Imported multiple CSV datasets
- Created SQLite database
- Loaded datasets using SQLAlchemy
- Added logging for monitoring ETL process

---

## 2️⃣ Data Cleaning

Performed:

- Missing value handling
- Data validation
- Duplicate checking
- Data type conversion
- Relationship validation across tables

---

## 3️⃣ SQL Data Integration

Built a consolidated **Vendor Sales Summary** table by integrating:

- Purchases
- Sales
- Purchase Prices
- Vendor Freight Costs
- Inventory Information

using SQL joins and aggregation queries.

---

## 4️⃣ Feature Engineering

Calculated key business KPIs including:

- Gross Profit
- Profit Margin (%)
- Stock Turnover Ratio
- Sales-to-Purchase Ratio
- Unsold Inventory Value
- Procurement Contribution (%)

---

## 5️⃣ Exploratory Data Analysis

Performed comprehensive EDA including:

- Summary Statistics
- Distribution Analysis
- Outlier Detection
- Correlation Analysis
- Vendor Performance Analysis
- Brand Performance Analysis
- Inventory Analysis
- Procurement Analysis
- Freight Cost Analysis
- Pareto Analysis

---

## 6️⃣ Statistical Analysis

Applied:

- 95% Confidence Interval
- Welch's Independent Two-Sample t-Test

to determine whether profit margins differ significantly between top-performing and low-performing vendors.

---

#  Key Business Insights

###  Procurement Analysis

- The **Top 10 vendors contribute approximately 65.69%** of total procurement expenditure.
- Procurement is highly concentrated among a limited number of suppliers, indicating potential supply chain dependency.

---

###  Inventory Analysis

- Approximately **$2.71 Million** is locked in unsold inventory.
- Several vendors exhibit low inventory turnover, indicating excess stock and slow-moving products.

---

###  Pricing Analysis

- Bulk purchasing generally reduces unit purchase price.
- Larger purchase volumes provide significant procurement cost savings.

---

###  Brand Analysis

- Identified **198 brands** with low sales but high profit margins.
- These brands represent opportunities for targeted marketing, promotional campaigns, and pricing optimization.

---

###  Statistical Findings

Welch's Independent t-test confirmed a statistically significant difference in profit margins between top-performing and low-performing vendors.

The analysis demonstrates that:

- Higher sales volume does not necessarily correspond to higher profit margins.
- Vendor performance should be evaluated using multiple KPIs rather than sales alone.

---

#  Visualizations Included

This project includes numerous business visualizations, including:

- Distribution Plots
- Box Plots
- Count Plots
- Correlation Heatmap
- Vendor Performance Charts
- Brand Performance Charts
- Procurement Contribution Analysis
- Pareto Chart
- Inventory Turnover Analysis
- Confidence Interval Plot
- Statistical Comparison Charts

---

#  Business Recommendations

Based on the analysis, the following recommendations are proposed:

- Diversify procurement across vendors to reduce supplier dependency.
- Improve inventory planning to minimize excess stock.
- Reduce capital locked in unsold inventory.
- Continue leveraging bulk purchasing for high-demand products.
- Promote high-margin, low-sales products through targeted marketing.
- Optimize freight costs by reviewing logistics strategies.
- Monitor vendor performance using multiple KPIs, including profitability, procurement contribution, and inventory turnover.
- Develop interactive dashboards for continuous performance monitoring.

---

#  Repository Structure

```
Inventory-Vendor-Performance-Analytics/
│
├── Exploratory_Data_Analysis.ipynb
├── Vendor_Performance_Analysis.ipynb
├── Data_Processing.ipynb
│
├── ingestion_db.py
├── get_vendor_summary.py
│
├── Inventory_Vendor_Analytics_Report.pdf
│
└── README.md
```

---

#  Project Screenshots

Below are some key analyses included in this project:

- Procurement Pareto Analysis
- Vendor Performance Dashboard
- Correlation Heatmap
- Inventory Turnover Analysis
- Statistical Hypothesis Testing
- Confidence Interval Analysis

*(Screenshots can be found in the repository.)*

---

#  Future Improvements

Future enhancements may include:

- Interactive Power BI Dashboard
- Tableau Dashboard
- Demand Forecasting using Machine Learning
- ABC Inventory Analysis
- Supplier Risk Assessment
- Automated ETL Pipeline
- Inventory Optimization Models

---

#  Project Report

A detailed project report documenting the methodology, exploratory analysis, statistical findings, business insights, and recommendations is included in this repository.

---

#  Author

**Aditya Sahu**

🎓 B.Tech Computer Science Engineering

📍 Delhi, India

🔗 **GitHub:** https://github.com/ADITYASAHU9868


---

## ⭐ Support

If you found this project helpful or interesting, consider **starring ⭐ the repository**. Your support is greatly appreciated!
---

## ⭐ If you found this project useful, consider giving it a star!
