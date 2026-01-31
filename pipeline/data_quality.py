import pandas as pd


def validate_sales_data(df: pd.DataFrame):
    """
    Perform basic data quality checks on transformed sales data.
    """

    if df.empty:
        raise ValueError("Data quality check failed: DataFrame is empty")

    required_columns = [
        "customer_id",
        "product_id",
        "order_date",
        "quantity",
        "total_amount"
    ]

    for col in required_columns:
        if col not in df.columns:
            raise ValueError(f"Data quality check failed: Missing column {col}")

    if (df["quantity"] <= 0).any():
        raise ValueError("Data quality check failed: Quantity contains non-positive values")

    if (df["total_amount"] <= 0).any():
        raise ValueError("Data quality check failed: Total amount contains non-positive values")

    return True
