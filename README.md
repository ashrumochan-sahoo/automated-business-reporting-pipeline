# Automated Sales Reporting Pipeline
Overview
This project implements a batch ETL pipeline using Python and SQL Server to process raw sales datasets into structured analytics tables for reporting and analysis.

The pipeline performs data extraction, cleansing, transformation, and loading, followed by SQL-based analytical queries to generate business insights.

Architecture
CSV Data → Python ETL → SQL Server → Analytics Queries

Tech Stack
- Python
- SQL Server
- Pandas
- SQL
- Shell Scripting
- Git

ETL Workflow

Extract
- Ingests raw sales data from CSV sources
- Performs basic validation and logging

Transform
- Cleans and standardizes raw datasets
- Handles null values and data type consistency
- Applies business-level transformations

Load
- Loads curated datasets into SQL Server
- Creates structured tables for analytics

Analytics
- Region-wise sales analysis
- Product-wise performance analysis
- Time-based sales trends using SQL

Automation
- Automated batch execution of the ETL pipeline using OS-level scheduling to simulate production-style data workflows

How to Run the Pipeline
1. Place the raw sales data file at: data/raw/sales_data.csv
2. (Optional) Create and activate a virtual environment:
    python -m venv venv
    source venv/bin/activate
3. Install required dependencies:
    pip install -r requirements.txt
4. Execute the end-to-end pipeline:
    ./scripts/run_pipeline.sh
