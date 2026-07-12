import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset
sales = pd.read_csv("data/processed/sales_cleaned.csv")

sales["InvoiceDate"] = pd.to_datetime(sales["InvoiceDate"])
sales["Month"] = sales["InvoiceDate"].dt.to_period("M").astype(str)

monthly_qty = (
    sales.groupby("Month")["Quantity"]
    .sum()
)

print("=" * 60)
print("MONTHLY QUANTITY SOLD")
print("=" * 60)
print(monthly_qty)

plt.figure(figsize=(12,6))

bars = plt.bar(
    monthly_qty.index,
    monthly_qty.values
)

plt.title("Monthly Quantity Sold")
plt.xlabel("Month")
plt.ylabel("Quantity")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(
    "outputs/monthly_quantity.png",
    dpi=300
)

plt.close()

print("\nGraph saved successfully.")