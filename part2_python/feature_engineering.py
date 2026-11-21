from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s")

logger = logging.getLogger(__name__)

df = pd.read_csv(
    "data/processed/traffic_clean.csv")

logger.info(
    f"Dataset shape before feature engineering: {df.shape}")

import numpy as np

df["date_time"] = pd.to_datetime(df["date_time"])

df["Hour"] = df["date_time"].dt.hour

df["Day_of_week"] = (df["date_time"].dt.day_name())

df["Weekend"] = (df["date_time"].dt.dayofweek >= 5).astype(int)

df["Hour_Sin"] = np.sin(2 * np.pi * df["Hour"] / 24)

df["Hour_Cos"] = np.cos(2 * np.pi * df["Hour"] / 24)

logger.info(
    "Time features created successfully")

logger.info(
    f"Dataset shape after feature engineering: {df.shape}")

from config import (
    SEVERE_WEATHER,
    LOW_VISIBILITY
)

df["Severe_Weather"] = (
    df["weather_main"]
    .isin(SEVERE_WEATHER)
).astype(int)

df["Low_Visibility"] = (
    df["weather_main"]
    .isin(LOW_VISIBILITY)
).astype(int)

logger.info(
    "Weather indicator features created")

logger.info(
    f"Dataset shape after weather features: {df.shape}")

scaler = MinMaxScaler()

df[["Temp_Scales", "Traffic_Scaled"]] = (
    scaler.fit_transform(
        df[["temp", "traffic_volume"]])
)

logger.info(
    "Numerical features scaled successfully")

logger.info(
    f"Dataset shape after scaling: {df.shape}")

q1 = df["traffic_volume"].quantile(0.25)
q2 = df["traffic_volume"].quantile(0.50)
q3 = df["traffic_volume"].quantile(0.75)

logger.debug(
    f"Traffic quartiles: Q1={q1}, Q2={q2}, Q3={q3}")

def congestion_category(volume):
    if volume < q1:
        return "Low"
    elif volume < q2:
        return "Medium"
    elif volume < q3:
        return "High"
    else:
        return "Severe"

df["Congestion_Category"] = (
    df["traffic_volume"]
    .apply(congestion_category)
)

high_congestion = (
    df["Congestion_Category"]
    .isin(
        ["High", "Severe"]
    )
)

risky_weather = (
    (df["Severe_Weather"] == 1)
    |
    (df["Low_Visibility"] == 1)
)

df["High_Risk"] = (
    high_congestion &
    risky_weather
).astype(int)

logger.info(
    "Data-driven congestion categoryies created"
)

logger.info(
    f"Dataset shape after congestion category: {df.shape}"
)

logger.info(
    "Proxy accident-risk label created"
)

logger.info(
    f"Dataset shape after risk label:{df.shape}"
)

df.to_csv(
    "data/processed/traffic_features.csv",
    index=False
)

logger.info(
    "Feature dataset saved to data/processed/traffic_features.csv"
)
