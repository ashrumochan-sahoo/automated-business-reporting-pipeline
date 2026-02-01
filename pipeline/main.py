from pipeline.extract import extract_sales_data
from pipeline.transform import transform_sales_data
from pipeline.load import load_sales_data
from pipeline.data_quality import validate_sales_data


def run_pipeline():
    raw_df = extract_sales_data("data/raw/sales_data.csv")
    tables = transform_sales_data(raw_df)

    validate_sales_data(tables["fact_sales"])

    load_sales_data(tables)


if __name__ == "__main__":
    run_pipeline()
