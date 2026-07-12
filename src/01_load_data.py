import pandas as pd

# Read the sales dataset
sales = pd.read_csv("data/raw/sales_transactions.csv")

# Display first 5 rows
print("\nFirst 5 Rows:\n")
print(sales.head())

# Display number of rows and columns
print("\nShape of Dataset:")
print(sales.shape)

# Display column names
print("\nColumn Names:")
print(sales.columns)