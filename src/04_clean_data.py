import pandas as pd

# Load the raw dataset
sales = pd.read_csv("data/raw/sales_transactions.csv")

print("=" * 60)
print("DATA CLEANING")
print("=" * 60)

print(f"Original Shape: {sales.shape}")

# Remove rows with missing CustomerID
sales = sales.dropna(subset=["CustomerID"])

# Keep only positive quantities
sales = sales[sales["Quantity"] > 0]

# Keep only positive TotalPrice
sales = sales[sales["TotalPrice"] > 0]

print(f"Cleaned Shape: {sales.shape}")

# Save the cleaned dataset
sales.to_csv("data/processed/sales_cleaned.csv", index=False)

print("\n✅ Cleaned dataset saved successfully!")