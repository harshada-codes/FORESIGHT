import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset
sales = pd.read_csv("data/processed/sales_cleaned.csv")

# Revenue by sales channel
channel_sales = (
    sales.groupby("Channel")["TotalPrice"]
    .sum()
    .sort_values(ascending=False)
)

print("=" * 60)
print("SALES CHANNEL ANALYSIS")
print("=" * 60)
print(channel_sales)

plt.figure(figsize=(8,5))

bars = plt.bar(
    channel_sales.index,
    channel_sales.values / 1_000_000
)

plt.title("Revenue by Sales Channel")
plt.xlabel("Channel")
plt.ylabel("Revenue (Million ₹)")

for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width()/2,
        height,
        f"{height:.2f}M",
        ha="center",
        va="bottom",
        fontsize=9
    )

plt.tight_layout()

plt.savefig(
    "outputs/channel_revenue.png",
    dpi=300
)

plt.close()

print("\nGraph saved successfully.")