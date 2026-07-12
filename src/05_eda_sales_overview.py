import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned data
sales = pd.read_csv("data/processed/sales_cleaned.csv")

# Convert InvoiceDate to datetime
sales["InvoiceDate"] = pd.to_datetime(sales["InvoiceDate"])

# Create a Month column
sales["Month"] = sales["InvoiceDate"].dt.to_period("M").astype(str)

# Group revenue by month
monthly_sales = sales.groupby("Month")["TotalPrice"].sum()

print(monthly_sales)

# Plot
plt.figure(figsize=(12, 6))
plt.plot(monthly_sales.index, monthly_sales.values, marker="o")
plt.title("Monthly Sales Revenue")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.grid(True)

# Save the chart
plt.savefig("outputs/monthly_sales.png", dpi=300)

# Display the chart
plt.show()