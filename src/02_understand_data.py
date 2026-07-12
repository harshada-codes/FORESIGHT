import pandas as pd

# Load the dataset
sales = pd.read_csv("data/raw/sales_transactions.csv")

print("=" * 50)
print("Dataset Information")
print("=" * 50)

# Display information about the dataset
print(sales.info())

print("\n" + "=" * 50)
print("Statistical Summary")
print("=" * 50)

# Display statistics
print(sales.describe())

print("\n" + "=" * 50)
print("Missing Values")
print("=" * 50)

# Check for missing values
print(sales.isnull().sum())