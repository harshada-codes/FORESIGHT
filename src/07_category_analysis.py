import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset
sales = pd.read_csv("data/processed/sales_cleaned.csv")

# Category-wise revenue
category_sales = (
    sales.groupby("Category")["TotalPrice"]
    .sum()
    .sort_values(ascending=False)
)

print("=" * 60)
print("CATEGORY-WISE REVENUE")
print("=" * 60)
print(category_sales)

# Plot
plt.figure(figsize=(10,6))

bars = plt.bar(
    category_sales.index,
    category_sales.values / 1_000_000
)

plt.title("Revenue by Category")
plt.xlabel("Category")
plt.ylabel("Revenue (Million ₹)")

plt.xticks(rotation=45)

# Add labels
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
    "outputs/category_revenue.png",
    dpi=300
)

plt.close()

print("\nGraph saved successfully.")