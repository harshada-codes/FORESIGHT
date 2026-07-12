import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset
sales = pd.read_csv("data/processed/sales_cleaned.csv")

corr = sales[["Quantity", "UnitPrice", "TotalPrice"]].corr()

print("=" * 60)
print("CORRELATION MATRIX")
print("=" * 60)
print(corr)

plt.figure(figsize=(6,5))

plt.imshow(corr, interpolation="nearest")

plt.colorbar()

plt.xticks(range(len(corr.columns)), corr.columns)
plt.yticks(range(len(corr.columns)), corr.columns)

for i in range(len(corr.columns)):
    for j in range(len(corr.columns)):
        plt.text(
            j,
            i,
            f"{corr.iloc[i,j]:.2f}",
            ha="center",
            va="center"
        )

plt.title("Correlation Heatmap")

plt.tight_layout()

plt.savefig(
    "outputs/correlation_heatmap.png",
    dpi=300
)

plt.close()

print("\nGraph saved successfully.")