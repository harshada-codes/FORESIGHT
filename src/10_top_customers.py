import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset
sales = pd.read_csv("data/processed/sales_cleaned.csv")

# Customer-wise revenue
top_customers = (
    sales.groupby("CustomerID")["TotalPrice"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("=" * 60)
print("TOP 10 CUSTOMERS BY REVENUE")
print("=" * 60)
print(top_customers)

plt.figure(figsize=(12,6))

bars = plt.bar(
    top_customers.index.astype(str),
    top_customers.values / 1_000_000
)

plt.title("Top 10 Customers by Revenue")
plt.xlabel("Customer ID")
plt.ylabel("Revenue (Million ₹)")

for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width()/2,
        height,
        f"{height:.2f}M",
        ha="center",
        va="bottom",
        fontsize=8
    )

plt.tight_layout()

plt.savefig(
    "outputs/top_customers.png",
    dpi=300
)

plt.close()

print("\nGraph saved successfully.")