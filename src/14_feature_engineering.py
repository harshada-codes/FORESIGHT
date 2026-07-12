import pandas as pd

print("=" * 60)
print("FEATURE ENGINEERING")
print("=" * 60)

# Load cleaned dataset
sales = pd.read_csv("data/processed/sales_cleaned.csv")

# Convert InvoiceDate to datetime
sales["InvoiceDate"] = pd.to_datetime(sales["InvoiceDate"])

# Date Features
sales["Year"] = sales["InvoiceDate"].dt.year
sales["Month"] = sales["InvoiceDate"].dt.month
sales["Day"] = sales["InvoiceDate"].dt.day
sales["DayOfWeek"] = sales["InvoiceDate"].dt.day_name()
sales["Quarter"] = sales["InvoiceDate"].dt.quarter
sales["Week"] = sales["InvoiceDate"].dt.isocalendar().week.astype(int)

# Weekend Flag
sales["IsWeekend"] = sales["InvoiceDate"].dt.dayofweek >= 5

# Revenue Per Unit
sales["RevenuePerUnit"] = sales["TotalPrice"] / sales["Quantity"]

# Order Value (Invoice Total)
invoice_total = (
    sales.groupby("Invoice")["TotalPrice"]
    .sum()
    .rename("InvoiceTotal")
)

sales = sales.merge(
    invoice_total,
    on="Invoice",
    how="left"
)

print("\nDataset Shape:")
print(sales.shape)

print("\nNew Columns Added:")
print([
    "Year",
    "Month",
    "Day",
    "DayOfWeek",
    "Quarter",
    "Week",
    "IsWeekend",
    "RevenuePerUnit",
    "InvoiceTotal"
])

# Save engineered dataset
sales.to_csv(
    "data/processed/feature_engineered_sales.csv",
    index=False
)

print("\n✅ Feature engineered dataset saved successfully.")