import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset
sales = pd.read_csv("data/processed/sales_cleaned.csv")

# Convert to datetime
sales["InvoiceDate"] = pd.to_datetime(sales["InvoiceDate"])

# Extract only the date
sales["Date"] = sales["InvoiceDate"].dt.date

# Daily revenue
daily_sales = (
    sales.groupby("Date")["TotalPrice"]
    .sum()
)

print("=" * 60)
print("DAILY SALES TREND")
print("=" * 60)
print(daily_sales.head())

plt.figure(figsize=(15,6))

plt.plot(
    daily_sales.index,
    daily_sales.values,
    linewidth=2
)

plt.title("Daily Sales Revenue")
plt.xlabel("Date")
plt.ylabel("Revenue (₹)")
plt.grid(True)

plt.tight_layout()

plt.savefig(
    "outputs/daily_sales_trend.png",
    dpi=300
)

plt.close()

print("\nGraph saved successfully.")