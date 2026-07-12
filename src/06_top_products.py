import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset
sales = pd.read_csv("data/processed/sales_cleaned.csv")

print("=" * 60)
print("TOP 10 PRODUCTS BY REVENUE")
print("=" * 60)

# Group by product description
top_products = (
    sales.groupby("Description")["TotalPrice"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\nTop 10 Products by Revenue (Million ₹)\n")

for product, revenue in top_products.items():
    print(f"{product:<35} : ₹{revenue/1_000_000:.2f} M")

# Plot
plt.figure(figsize=(12,6))

bars = plt.bar(
    top_products.index,
    top_products.values / 1_000_000
)

plt.title("Top 10 Products by Revenue")
plt.xlabel("Product")
plt.ylabel("Revenue (Million ₹)")

plt.xticks(rotation=45, ha="right")

# Add values above bars
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

plt.savefig("outputs/top_10_products.png", dpi=300)

plt.close()