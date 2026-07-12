"""
FORESIGHT
Inventory Recommendation Engine
"""

from pathlib import Path
import pandas as pd

OUTPUT_DIR = Path("outputs")
OUTPUT_DIR.mkdir(exist_ok=True)


def load_inventory():
    return pd.read_csv("data/raw/inventory_daily.csv")


def create_recommendations(df):
    # Use the latest inventory record for each SKU
    latest = (
        df.sort_values("Date")
          .groupby("StockCode")
          .tail(1)
          .copy()
    )

    latest["Recommendation"] = "Healthy Stock"

    # Priority 1: Existing stockout
    latest.loc[
        latest["Stockout"] == 1,
        "Recommendation"
    ] = "URGENT REORDER"

    # Priority 2: Closing stock below reorder point
    latest.loc[
        (latest["ClosingStock"] <= latest["ReorderPoint"]) &
        (latest["Stockout"] == 0),
        "Recommendation"
    ] = "Reorder Soon"

    # Priority 3: Overstock
    latest.loc[
        latest["ClosingStock"] > latest["TargetStock"],
        "Recommendation"
    ] = "Overstock"

    # Priority 4: Lost sales detected
    latest.loc[
        latest["LostSales"] > 0,
        "Recommendation"
    ] = "Investigate Demand"

    return latest


def main():

    print("=" * 60)
    print("INVENTORY RECOMMENDATION ENGINE")
    print("=" * 60)

    inventory = load_inventory()

    recommendations = create_recommendations(inventory)

    recommendations.to_csv(
        OUTPUT_DIR / "inventory_recommendations.csv",
        index=False
    )

    print("\nRecommendation Summary\n")
    print(recommendations["Recommendation"].value_counts())

    print("\nSample\n")
    print(
        recommendations[
            [
                "StockCode",
                "ClosingStock",
                "ReorderPoint",
                "TargetStock",
                "Recommendation"
            ]
        ].head(15)
    )

    print("\nSaved:")
    print("outputs/inventory_recommendations.csv")


if __name__ == "__main__":
    main()