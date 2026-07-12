# 📊 FORESIGHT – AI Powered Retail Analytics Dashboard

![Dashboard](screenshots/dashboard.png)

An end-to-end AI-powered Retail Analytics platform developed using **Python, Machine Learning, and Streamlit** during the **Zidio Development Internship**.

The dashboard helps businesses analyze sales performance, identify customer behavior, forecast future demand, optimize inventory, and detect customer churn risk through interactive visualizations and machine learning models.

---

# 🚀 Features

### 📈 Sales Analytics
- Monthly Revenue Trend
- Top 10 Products by Revenue
- Category-wise Revenue Analysis
- Country-wise Revenue Analysis
- Sales Channel Distribution
- Daily Sales Trend
- Quantity Analysis

### 👥 Customer Analytics
- Top Customers
- RFM Customer Segmentation
- Customer Churn Risk Analysis
- Executive AI Summary

### 🤖 AI & Machine Learning
- Demand Forecasting using Random Forest Regressor
- Inventory Recommendation Engine
- Customer Segmentation using RFM Analysis
- Feature Engineering Pipeline

### 📊 Interactive Dashboard
- Dynamic Sidebar Filters
- KPI Cards
- Interactive Plotly Charts
- Download Reports (CSV)
- AI Business Insights

---

# 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Plotly
- Streamlit
- Scikit-learn
- Random Forest Regressor

---

# 📁 Project Structure

```
FORESIGHT/
│
├── app/
│   └── app.py
│
├── data/
│   ├── raw/
│   └── processed/
│
├── outputs/
│   ├── forecast.csv
│   ├── inventory_recommendations.csv
│   └── customer_churn_risk.csv
│
├── src/
│   ├── 01_load_data.py
│   ├── 02_understand_data.py
│   ├── 03_data_quality.py
│   ├── 04_clean_data.py
│   ├── 05_eda_sales_overview.py
│   ├── 06_top_products.py
│   ├── 07_category_analysis.py
│   ├── 08_country_analysis.py
│   ├── 09_channel_analysis.py
│   ├── 10_top_customers.py
│   ├── 11_daily_sales_trend.py
│   ├── 12_quantity_analysis.py
│   ├── 13_correlation_heatmap.py
│   ├── 14_feature_engineering.py
│   ├── 15_rfm_segmentation.py
│   ├── forecasting.py
│   ├── inventory.py
│   ├── churn.py
│   └── data_loader.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 📊 Dashboard Overview

The dashboard provides:

- 📌 Executive KPI Cards
- 📈 Monthly Revenue Trend
- 🏆 Top Products Analysis
- 🛍 Revenue by Category
- 🌍 Revenue by Country
- 📱 Sales Channel Distribution
- 🤖 Executive AI Summary
- 👥 Customer Segmentation
- 🚨 Customer Churn Risk
- 📈 30-Day Demand Forecast
- 📦 Inventory Recommendations
- 📥 Downloadable Reports

---

# 🧠 Machine Learning Modules

## Demand Forecasting
- Model: Random Forest Regressor
- Predicts future daily sales revenue.

## Customer Segmentation
- RFM Analysis
- Segments customers into:
  - Champions
  - Loyal Customers
  - Potential Loyalists
  - At Risk
  - Lost Customers

## Customer Churn Prediction
Customers are classified into:
- High Risk
- Medium Risk
- Low Risk

## Inventory Recommendation
Generates inventory recommendations:
- Healthy Stock
- Reorder Soon
- Overstock

---

# ▶️ Installation

Clone the repository

```bash
git clone <repository-url>
```

Move into the project

```bash
cd FORESIGHT
```

Create virtual environment

```bash
python -m venv venv
```

Activate virtual environment

### Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the dashboard

```bash
streamlit run app/app.py
```

---

# 📷 Dashboard Screenshots

## 🏠 Dashboard Overview

![Dashboard Overview](screenshots/dashboard.png)

---

## 📈 Monthly Revenue Trend

![Monthly Revenue Trend](screenshots/monthly_revenue_trend.png)

---

## 🏆 Top 10 Products by Revenue

![Top Products](screenshots/top_products.png)

---

## 🌍 Revenue by Category & Country

![Revenue by Category and Country](screenshots/category_country_revenue.png)

---

## 🛒 Sales Channel Distribution

![Sales Channel Distribution](screenshots/sales_channel.png)

---

## 🤖 Executive AI Summary

![Executive AI Summary](screenshots/executive_ai_summary.png)

---

## 📅 30-Day Sales Forecast

![30-Day Sales Forecast](screenshots/sales_forecast.png)

---

## 📦 Inventory Recommendations

![Inventory Recommendations](screenshots/inventory_recommendations.png)

---

## 📥 Download Reports

![Download Reports](screenshots/download_reports.png)

---

# 📈 Future Enhancements

- Authentication & Login
- Real-time Database Integration
- Cloud Deployment
- Sales Prediction API
- Customer Lifetime Value Prediction
- Automated Email Reports
- Power BI Integration

---

# 👩‍💻 Developer

**Harshada Patil**

BE Computer Engineering

Jawahar Education Society's Institute of Technology, Management & Research, Nashik

Developed as part of the **Zidio Development Internship**.

---

# 📄 License

This project is developed for educational and internship purposes.

© 2026 Harshada Patil