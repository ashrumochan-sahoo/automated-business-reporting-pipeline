import pyodbc
import pandas as pd


def load_sales_data(tables: dict):
    """
    Load fact and dimension tables into SQL Server.
    """
    
conn = pyodbc.connect(
    "DRIVER={ODBC Driver 18 for SQL Server};"
    "SERVER=localhost,1433;"
    "DATABASE=sales_db;"
    "UID=sa;"
    "PWD=StrongP@ssw0rd!;"
    "TrustServerCertificate=yes;"
)

    print("SQL Server connection successful")

    cursor = conn.cursor()

    # ------------------------------------
    # Load Dimension: Customer
    # ------------------------------------
    cursor.fast_executemany = True
    cursor.executemany(
        """
        INSERT INTO dim_customer (customer_id, customer_name, region, country)
        VALUES (?, ?, ?, ?)
        """,
        tables["dim_customer"].values.tolist()
    )

    # ------------------------------------
    # Load Dimension: Product
    # ------------------------------------
    cursor.executemany(
        """
        INSERT INTO dim_product (product_id, product_name, category, sub_category)
        VALUES (?, ?, ?, ?)
        """,
        tables["dim_product"].values.tolist()
    )

    # ------------------------------------
    # Load Dimension: Date
    # ------------------------------------
    cursor.executemany(
        """
        INSERT INTO dim_date (date_id, full_date, year, month, day, weekday)
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        tables["dim_date"].values.tolist()
    )

    # ------------------------------------
    # Load Fact: Sales
    # ------------------------------------
    cursor.executemany(
        """
        INSERT INTO fact_sales (date_id, customer_id, product_id, quantity, total_amount)
        VALUES (?, ?, ?, ?, ?)
        """,
        tables["fact_sales"].values.tolist()
    )

    conn.commit()
    cursor.close()
    conn.close()
