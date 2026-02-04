import pyodbc
import pandas as pd


def load_fact_sales(df: pd.DataFrame, connection_string: str) -> None:
    """
    Load transformed sales data into fact_sales table in SQL Server.

    Args:
        df (pd.DataFrame): Transformed sales dataframe
        connection_string (str): SQL Server connection string
    """

    # Connect to SQL Server
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()

    print("SQL Server connection successful")

    insert_query = """
        INSERT INTO fact_sales (
            sales_id,
            date_id,
            customer_id,
            product_id,
            quantity,
            total_amount
        )
        VALUES (?, ?, ?, ?, ?, ?)
    """

    # Insert rows
    for index, row in df.iterrows():
        cursor.execute(
            insert_query,
            int(index),
            int(row["order_date"].strftime("%Y%m%d")),
            int(row["customer_id"]),
            int(row["product_id"]),
            int(row["quantity"]),
            float(row["total_amount"])
        )

    conn.commit()
    cursor.close()
    conn.close()

    print("Data loaded successfully into fact_sales")
