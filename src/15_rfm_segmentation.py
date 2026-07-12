import pandas as pd

print("=" * 60)
print("RFM CUSTOMER SEGMENTATION")
print("=" * 60)

# Load feature engineered dataset
sales = pd.read_csv("data/processed/feature_engineered_sales.csv")

sales["InvoiceDate"] = pd.to_datetime(sales["InvoiceDate"])

# Reference date
snapshot_date = sales["InvoiceDate"].max() + pd.Timedelta(days=1)

# Create RFM table
rfm = sales.groupby("CustomerID").agg(
    Recency=("InvoiceDate", lambda x: (snapshot_date - x.max()).days),
    Frequency=("Invoice", "nunique"),
    Monetary=("TotalPrice", "sum")
)

# RFM Scores
rfm["R_Score"] = pd.qcut(
    rfm["Recency"],
    4,
    labels=[4,3,2,1]
).astype(int)

rfm["F_Score"] = pd.qcut(
    rfm["Frequency"].rank(method="first"),
    4,
    labels=[1,2,3,4]
).astype(int)

rfm["M_Score"] = pd.qcut(
    rfm["Monetary"],
    4,
    labels=[1,2,3,4]
).astype(int)

rfm["RFM_Score"] = (
    rfm["R_Score"].astype(str)
    + rfm["F_Score"].astype(str)
    + rfm["M_Score"].astype(str)
)

# Customer Segments
def segment(row):
    if row["R_Score"] >= 4 and row["F_Score"] >= 4:
        return "Champions"

    elif row["F_Score"] >= 4:
        return "Loyal Customers"

    elif row["R_Score"] >= 3:
        return "Potential Loyalists"

    elif row["R_Score"] == 2:
        return "At Risk"

    else:
        return "Lost Customers"

rfm["Segment"] = rfm.apply(segment, axis=1)

print("\nCustomer Segments\n")
print(rfm["Segment"].value_counts())

rfm.to_csv(
    "data/processed/rfm_segments.csv"
)

print("\nSaved:")
print("data/processed/rfm_segments.csv")