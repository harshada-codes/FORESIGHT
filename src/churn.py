"""
FORESIGHT
Customer Churn Risk Engine
"""

from pathlib import Path
import pandas as pd

OUTPUT_DIR = Path("outputs")
OUTPUT_DIR.mkdir(exist_ok=True)


def load_rfm():
    return pd.read_csv("data/processed/rfm_segments.csv")


def assign_risk(segment):
    if segment == "Lost Customers":
        return "High Risk"

    elif segment == "At Risk":
        return "High Risk"

    elif segment == "Potential Loyalists":
        return "Medium Risk"

    elif segment == "Loyal Customers":
        return "Low Risk"

    elif segment == "Champions":
        return "Low Risk"

    return "Medium Risk"


def main():

    print("=" * 60)
    print("CUSTOMER CHURN RISK")
    print("=" * 60)

    rfm = load_rfm()

    rfm["ChurnRisk"] = rfm["Segment"].apply(assign_risk)

    rfm.to_csv(
        OUTPUT_DIR / "customer_churn_risk.csv",
        index=False
    )

    print("\nRisk Summary\n")
    print(rfm["ChurnRisk"].value_counts())

    print("\nTop Customers\n")
    print(
        rfm[
            [
                "Recency",
                "Frequency",
                "Monetary",
                "Segment",
                "ChurnRisk",
            ]
        ].head(15)
    )

    print("\nSaved:")
    print("outputs/customer_churn_risk.csv")


if __name__ == "__main__":
    main()