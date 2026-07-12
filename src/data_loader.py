"""
FORESIGHT
Data Loading Module
"""

import pandas as pd


PROCESSED_DATA = "data/processed/feature_engineered_sales.csv"


def load_sales_data():
    """
    Load the processed sales dataset.
    """

    sales = pd.read_csv(PROCESSED_DATA)

    sales["InvoiceDate"] = pd.to_datetime(
        sales["InvoiceDate"]
    )

    return sales


if __name__ == "__main__":

    df = load_sales_data()

    print("=" * 60)
    print("DATASET LOADED")
    print("=" * 60)

    print(df.head())

    print("\nShape:", df.shape)