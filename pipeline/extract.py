import os
import pandas as pd


def extract_sales_data(file_path: str) -> pd.DataFrame:
    """
    Extract raw sales data from CSV file.

    Args:
        file_path (str): Path to raw sales CSV file

    Returns:
        pd.DataFrame: Raw sales data
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Input file not found: {file_path}")

    df = pd.read_csv(file_path)

    if df.empty:
        raise ValueError("Extracted data is empty")

    return df
