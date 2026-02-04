import pandas as pd


def transform_sales_data(raw_df: pd.DataFrame) -> dict:
    """
    Transform Global Superstore raw sales data into
    fact and dimension tables.

    Returns:
        dict: DataFrames for fact_sales and dimension tables
    """

    df = raw_df.copy()

    # ------------------------------------
    # Step 1: Normalize column names
    # ------------------------------------
    df.columns = (
        df.columns
        .str.lower()
        .str.replace(" ", "_")
        .str.replace("-", "_")
    )

    # ------------------------------------
    # Step 2: Select required columns
    # ------------------------------------
    df = df[[
        "order_date",
        "customer_id",
        "customer_name",
        "region",
        "country",
        "product_id",
        "product_name",
        "category",
        "sub_category",
        "sales",
        "quantity"
    ]]

    # ------------------------------------
    # Step 3: Data type conversions
    # ------------------------------------
    df["order_date"] = pd.to_datetime(df["order_date"])
    df["quantity"] = df["quantity"].astype(int)
    df["sales"] = df["sales"].astype(float)

    # ------------------------------------
    # Step 4: Derive metrics
    # ------------------------------------
    df["total_amount"] = df["sales"]
    df["date_id"] = df["order_date"].dt.strftime("%Y%m%d").astype(int)

    # ------------------------------------
    # Step 5: Build dimension tables
    # ------------------------------------
    dim_customer = df[[
        "customer_id",
        "customer_name",
        "region",
        "country"
    ]].drop_duplicates()

    dim_product = df[[
        "product_id",
        "product_name",
        "category",
        "sub_category"
    ]].drop_duplicates()

    dim_date = df[["date_id", "order_date"]].drop_duplicates()
    dim_date["year"] = dim_date["order_date"].dt.year
    dim_date["month"] = dim_date["order_date"].dt.month
    dim_date["day"] = dim_date["order_date"].dt.day
    dim_date["weekday"] = dim_date["order_date"].dt.day_name()

    # ------------------------------------
    # Step 6: Build fact table
    # ------------------------------------
    fact_sales = df[[
        "date_id",
        "customer_id",
        "product_id",
        "quantity",
        "total_amount"
    ]]

    # ------------------------------------
    # Step 7: Return structured output
    # ------------------------------------
    return {
        "dim_customer": dim_customer_df,
        "dim_product": dim_product_df,
        "dim_date": dim_date_df,
        "fact_sales": fact_sales_df
}

