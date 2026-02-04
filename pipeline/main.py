from pipeline.extract import extract_sales_data
from pipeline.transform import transform_sales_data
from pipeline.load import load_fact_sales

CONNECTION_STRING = (
    "DRIVER={ODBC Driver 18 for SQL Server};"
    "SERVER=localhost,1433;"
    "DATABASE=sales_db;"
    "UID=sa;"
    "PWD=StrongP@ssw0rd!;"
    "TrustServerCertificate=yes;"
)

def run_pipeline():
    raw_df = extract_sales_data("data/raw/sales_data.csv")
    transformed_df = transform_sales_data(raw_df)
    load_fact_sales(transformed_df, CONNECTION_STRING)

if __name__ == "__main__":
    run_pipeline()
