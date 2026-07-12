import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset
sales = pd.read_csv("data/processed/sales_cleaned.csv")

# Country-wise revenue
country_sales = (
    sales.groupby("Country")["TotalPrice"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("=" * 60)
print("TOP 10 COUNTRIES BY REVENUE")
print("=" * 60)
print(country_sales)

plt.figure(figsize=(12,6))

bars = plt.bar(
    country_sales.index,
    country_sales.values / 1_000_000
)

plt.title("Top 10 Countries by Revenue")
plt.xlabel("Country")
plt.ylabel("Revenue (Million ₹)")
plt.xticks(rotation=45)

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
    "outputs/top_10_countries.png",
    dpi=300
)

plt.close()

print("\nGraph saved successfully.")