import pandas as pd


def transform_sales_data(raw_df: pd.DataFrame) -> pd.DataFrame:
    """
    Transform raw sales data into analytics-ready format.

    Args:
        raw_df (pd.DataFrame): Raw extracted sales data

    Returns:
        pd.DataFrame: Transformed sales data
    """
    df = raw_df.copy()

    # Standardize column names
    df.columns = [col.lower() for col in df.columns]

    # Drop records with missing critical fields
    required_columns = [
        "customer_id",
        "product_id",
        "order_date",
        "quantity",
        "unit_price"
    ]
    df = df.dropna(subset=required_columns)

    # Convert data types
    df["quantity"] = df["quantity"].astype(int)
    df["unit_price"] = df["unit_price"].astype(float)

    # Create derived metric
    df["total_amount"] = df["quantity"] * df["unit_price"]

    return df
