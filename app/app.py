import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

st.set_page_config(
    page_title="FORESIGHT AI Retail Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 FORESIGHT")

st.markdown("""
### AI-Powered Retail Analytics Dashboard

Analyze sales performance, forecast demand, optimize inventory, and identify customer churn using machine learning insights.
""")

# ----------------------------
# Cached Data Loaders
# ----------------------------

@st.cache_data
def load_sales():
    return pd.read_csv("data/processed/feature_engineered_sales.csv")

@st.cache_data
def load_rfm():
    return pd.read_csv("data/processed/rfm_segments.csv")

@st.cache_data
def load_forecast():
    path = Path("outputs/forecast.csv")
    if path.exists():
        return pd.read_csv(path)
    return None

@st.cache_data
def load_inventory():
    path = Path("outputs/inventory_recommendations.csv")
    if path.exists():
        return pd.read_csv(path)
    return None

@st.cache_data
def load_churn():
    path = Path("outputs/customer_churn_risk.csv")
    if path.exists():
        return pd.read_csv(path)
    return None


sales = load_sales()
rfm = load_rfm()
forecast = load_forecast()
inventory = load_inventory()
churn = load_churn()

from datetime import datetime

st.info(
    f"""
📊 **Dataset Records:** {len(sales):,} &nbsp;&nbsp;&nbsp;
👥 **Customers:** {sales['CustomerID'].nunique():,} &nbsp;&nbsp;&nbsp;
📦 **Products:** {sales['StockCode'].nunique():,} &nbsp;&nbsp;&nbsp;
🕒 **Last Updated:** {datetime.now().strftime('%d %b %Y %I:%M %p')}
"""
)

sales["InvoiceDate"] = pd.to_datetime(sales["InvoiceDate"])

# ----------------------------
# Sidebar Filters
# ----------------------------

st.sidebar.title("📊 Dashboard Controls")

st.sidebar.markdown("---")

st.sidebar.header("🔍 Filters")

country_options = sorted(sales["Country"].unique())

country = st.sidebar.multiselect(
    "Country",
    country_options,
    default=country_options
)

if not country:
    country = country_options

category_options = sorted(sales["Category"].unique())

category = st.sidebar.multiselect(
    "Category",
    category_options,
    default=category_options
)

if not category:
    category = category_options

channel_options = sorted(sales["Channel"].unique())

channel = st.sidebar.multiselect(
    "Channel",
    channel_options,
    default=channel_options
)

if not channel:
    channel = channel_options

filtered = sales[
    sales["Country"].isin(country)
    & sales["Category"].isin(category)
    & sales["Channel"].isin(channel)
]

if filtered.empty:
    st.warning("⚠️ No data available for the selected filters.")
    st.stop()

# ----------------------------
# KPI Cards
# ----------------------------

revenue = filtered["TotalPrice"].sum()
orders = filtered["Invoice"].nunique()
customers = filtered["CustomerID"].nunique()
avg_order = revenue / orders

c1, c2, c3, c4 = st.columns(4)

c1.metric(
    label="💰 Total Revenue",
    value=f"₹{revenue:,.0f}"
)

c2.metric(
    label="🧾 Total Orders",
    value=f"{orders:,}"
)

c3.metric(
    label="👥 Total Customers",
    value=f"{customers:,}"
)

c4.metric(
    label="🛒 Avg Order Value",
    value=f"₹{avg_order:,.2f}"
)

st.caption(
    "📌 KPI values update automatically based on the selected filters."
)

st.divider()

# ----------------------------
# Monthly Sales
# ----------------------------

monthly = (
    filtered
    .groupby(filtered["InvoiceDate"].dt.to_period("M").astype(str))
    ["TotalPrice"]
    .sum()
    .reset_index()
)

fig = px.line(
    monthly,
    x="InvoiceDate",
    y="TotalPrice",
    markers=True,
    title="📈 Monthly Revenue Trend",
    template="plotly_white"
)

fig.update_traces(line=dict(width=3))

st.plotly_chart(
    fig,
    use_container_width=True,
    config={"displayModeBar": False}
)

# ----------------------------
# Top Products
# ----------------------------

top_products = (
    filtered
    .groupby("Description")["TotalPrice"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

fig = px.bar(
    top_products,
    x="Description",
    y="TotalPrice",
    title="🏆 Top 10 Products by Revenue",
    color="TotalPrice",
    template="plotly_white"
)

st.plotly_chart(
    fig,
    use_container_width=True,
    config={"displayModeBar": False}
)

col1, col2 = st.columns(2)

# ---------------- Category Revenue ----------------
with col1:

    category_data = (
        filtered.groupby("Category")["TotalPrice"]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
    )

    fig = px.bar(
        category_data,
        x="Category",
        y="TotalPrice",
        color="Category",
        title="🛍 Revenue by Category",
        template="plotly_white"
    )

    st.plotly_chart(
    fig,
    use_container_width=True,
    config={"displayModeBar": False}
)

# ---------------- Country Revenue ----------------
with col2:

    country_data = (
        filtered.groupby("Country")["TotalPrice"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )

    fig = px.bar(
        country_data,
        x="Country",
        y="TotalPrice",
        color="Country",
        title="🌍 Revenue by Country",
        template="plotly_white"
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
        config={"displayModeBar": False}
    )

channel_data = (
    filtered.groupby("Channel")["TotalPrice"]
    .sum()
    .reset_index()
)

fig = px.pie(
    channel_data,
    names="Channel",
    values="TotalPrice",
    title="📱 Sales by Channel",
    template="plotly_white"
)

st.plotly_chart(
    fig,
    use_container_width=True,
    config={"displayModeBar": False}
)

st.header("🤖 AI Insights")

# ==========================
# Executive AI Summary
# ==========================

best_category = (
    filtered.groupby("Category")["TotalPrice"]
    .sum()
    .idxmax()
)

best_country = (
    filtered.groupby("Country")["TotalPrice"]
    .sum()
    .idxmax()
)

best_channel = (
    filtered.groupby("Channel")["TotalPrice"]
    .sum()
    .idxmax()
)

largest_segment = (
    rfm["Segment"]
    .value_counts()
    .idxmax()
)

high_risk = (
    churn["ChurnRisk"] == "High Risk"
).sum()

st.subheader("🧠 Executive AI Summary")

st.caption(
    "Quick business insights generated automatically from the selected data."
)

col1, col2, col3, col4, col5 = st.columns([1, 1, 1, 1.2, 1])

with col1:
    st.info(f"🏆 **Top Category**\n\n{best_category}")

with col2:
    st.info(f"🌍 **Top Country**\n\n{best_country}")

with col3:
    st.info(f"🛒 **Top Sales Channel**\n\n{best_channel}")

with col4:
    st.info(f"👥 **Top Segment**\n\n{largest_segment}")

with col5:
    st.warning(f"🚨 **High-Risk**\n\n{high_risk:,} Customers")

st.divider()

col1, col2 = st.columns(2)

with col1:

    segment_data = (
        rfm["Segment"]
        .value_counts()
        .reset_index()
    )

    segment_data.columns = ["Segment", "Customers"]

    fig = px.pie(
        segment_data,
        names="Segment",
        values="Customers",
        title="Customer Segments"
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
        config={"displayModeBar": False}
    )
with col2:

    if churn is not None:

        churn_data = (
            churn["ChurnRisk"]
            .value_counts()
            .reset_index()
        )

        churn_data.columns = ["Risk", "Customers"]

        fig = px.bar(
            churn_data,
            x="Risk",
            y="Customers",
            color="Risk",
            title="Customer Churn Risk"
        )

        st.plotly_chart(
            fig,
            use_container_width=True,
            config={"displayModeBar": False}
        )

if forecast is not None:

    st.subheader("📈 30-Day Sales Forecast")

    st.info(
        "This forecast estimates the expected sales revenue for the next 30 days based on historical sales patterns."
    )

    fig = px.line(
        forecast,
        x="Date",
        y="ForecastRevenue",
        markers=True,
        title="Predicted Revenue for the Next 30 Days"
    )

    fig.update_layout(
        xaxis_title="Date",
        yaxis_title="Forecast Revenue",
        hovermode="x unified"
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
        config={"displayModeBar": False}
    )

if inventory is not None:

    st.subheader("📦 Inventory Recommendations")

    inventory_display = inventory[
        [
            "StockCode",
            "ClosingStock",
            "Recommendation"
        ]
    ].head(20).copy()

    inventory_display["Recommendation"] = (
        inventory_display["Recommendation"]
        .replace({
            "Healthy Stock": "🟢 Healthy Stock",
            "Reorder Soon": "🟡 Reorder Soon",
            "Overstock": "🔴 Overstock",
            "URGENT REORDER": "🚨 URGENT REORDER"
        })
    )

    st.dataframe(
        inventory_display,
        use_container_width=True
    )

st.header("📥 Download Reports")

st.caption("Download generated reports for further analysis.")

c1, c2, c3 = st.columns(3)

if forecast is not None:

    with c1:

        st.download_button(
            "📥 Download Forecast CSV",
            forecast.to_csv(index=False),
            "forecast.csv"
        )

if inventory is not None:

    with c2:

        st.download_button(
            "📥 Download Inventory CSV",
            inventory.to_csv(index=False),
            "inventory.csv"
        )

if churn is not None:

    with c3:

        st.download_button(
            "📥 Download Churn Report",
            churn.to_csv(index=False),
            "customer_churn.csv"
        )

# =====================================================
# Footer
# =====================================================

st.divider()

st.success("✅ Dashboard generated successfully. All insights are based on the selected filters.")

st.markdown("""
### 👨‍💻 Developed by Harshada Patil

**FORESIGHT – AI Powered Retail Analytics Platform**

• Python • Pandas • Plotly • Streamlit • Scikit-Learn

---
© 2026 | Zidio Development Internship • Version 1.0
""")