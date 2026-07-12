import pandas as pd

# Load dataset
sales = pd.read_csv("data/raw/sales_transactions.csv")

print("=" * 60)
print("DATA QUALITY REPORT")
print("=" * 60)

# Duplicate records
duplicates = sales.duplicated().sum()
print(f"\nDuplicate Rows: {duplicates}")

# Negative Quantity
negative_qty = (sales["Quantity"] < 0).sum()
print(f"Negative Quantity Rows: {negative_qty}")

# Negative Total Price
negative_total = (sales["TotalPrice"] < 0).sum()
print(f"Negative Total Price Rows: {negative_total}")

# Missing values
print("\nMissing Values")
print(sales.isnull().sum())