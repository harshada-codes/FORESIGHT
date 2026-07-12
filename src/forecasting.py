"""
FORESIGHT
Demand Forecasting using Random Forest
"""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.ensemble import RandomForestRegressor

from data_loader import load_sales_data

OUTPUT_DIR = Path("outputs")
OUTPUT_DIR.mkdir(exist_ok=True)


def prepare_data():
    sales = load_sales_data()

    daily = (
        sales.groupby(sales["InvoiceDate"].dt.date)["TotalPrice"]
        .sum()
        .reset_index()
    )

    daily.columns = ["Date", "Revenue"]
    daily["Date"] = pd.to_datetime(daily["Date"])

    daily["Day"] = daily["Date"].dt.day
    daily["Month"] = daily["Date"].dt.month
    daily["Year"] = daily["Date"].dt.year
    daily["DayOfWeek"] = daily["Date"].dt.dayofweek

    return daily


def train_model(df):
    X = df[["Day", "Month", "Year", "DayOfWeek"]]
    y = df["Revenue"]

    model = RandomForestRegressor(
        n_estimators=200,
        random_state=42
    )

    model.fit(X, y)

    return model


def forecast_next_30_days(model, df):

    last_date = df["Date"].max()

    future_dates = pd.date_range(
        last_date + pd.Timedelta(days=1),
        periods=30
    )

    future = pd.DataFrame({
        "Date": future_dates
    })

    future["Day"] = future["Date"].dt.day
    future["Month"] = future["Date"].dt.month
    future["Year"] = future["Date"].dt.year
    future["DayOfWeek"] = future["Date"].dt.dayofweek

    future["ForecastRevenue"] = model.predict(
        future[["Day", "Month", "Year", "DayOfWeek"]]
    )

    return future


def save_results(future):

    future.to_csv(
        OUTPUT_DIR / "forecast.csv",
        index=False
    )

    plt.figure(figsize=(14,6))

    plt.plot(
        future["Date"],
        future["ForecastRevenue"],
        linewidth=2
    )

    plt.title("30-Day Revenue Forecast")

    plt.xlabel("Date")
    plt.ylabel("Revenue")

    plt.grid(True)

    plt.tight_layout()

    plt.savefig(
        OUTPUT_DIR / "forecast.png",
        dpi=300
    )

    plt.close()


def main():

    print("=" * 60)
    print("RANDOM FOREST DEMAND FORECAST")
    print("=" * 60)

    df = prepare_data()

    model = train_model(df)

    future = forecast_next_30_days(model, df)

    save_results(future)

    print("\nForecast Complete")

    print(future.head())

    print("\nSaved:")

    print("outputs/forecast.csv")

    print("outputs/forecast.png")


if __name__ == "__main__":
    main()