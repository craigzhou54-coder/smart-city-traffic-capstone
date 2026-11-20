import pandas as pd
import logging

logging.basicConfig(
    level=logging.INFO, 
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    handlers=[
        logging.FileHandler(
            "logs/pipeline.log"
        ),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

try:
    logger.info("Pipeline started")
    df = pd.read_csv("../data/Metro_Interstate_Traffic_Volume.csv")
    logger.info(f"Rows loaded: {len(df)}")  
    logger.info(f"Columns loaded: {len(df.columns)}")
except FileNotFoundError:
    logger.error("CSV file not found")
except pd.errors.ParserError:
    logger.error("CSV parsing failed")

expected_columns = ["holiday", "temp", "rain_1h", "snow_1h", "clouds_all", "weather_main", "weather_description", "date_time", "traffic_volume"]
missing_columns = [col for col in expected_columns if col not in df.columns]
if missing_columns:
    logger.error(f"Missing columns: {missing_columns}")
else:
    logger.info("Schema validation passed")

logger.info(f"Column names: {list(df.columns)}")
duplicate_count = (df["date_time"].duplicated().sum())

logger.info(f"Duplicate timestamps found: {duplicate_count}")
unique_duplicate_timestamps = (
    df[df["date_time"].duplicated(keep=False)]
    ["date_time"].unique())

logger.info(f"Unique duplicated timestamps: {unique_duplicate_timestamps}")
duplicate_rows = (
    df[df["date_time"].duplicated(keep=False)])

logger.info(f"Rows involved in duplicate timestamps: {len(duplicate_rows)}")
duplicate_records = (df[df["date_time"].duplicated(keep=False)]
                     .sort_values("date_time"))

logger.info(f"Showing first 10 duplicate rows")
print(duplicate_records.head(10))

logger.info("Inspecting duplicate timestamp records")
Duplicate_records = (df[df["date_time"].duplicated(keep=False)]
                        .sort_values("date_time"))
print(duplicate_records[
    [
        "date_time",
        "temp",
        "rain_1h",
        "snow_1h",
        "clouds_all",
        "weather_main",
        "weather_description",
        "traffic_volume"
    ]
].head(20))

hourly_rows = (df["date_time"].nunique())
logger.info(f"Unique hourly timestamps: {hourly_rows}")

hourly_df = (df.groupby("date_time")
             .agg({
                 "holiday": "first",
                 "temp": "mean",
                 "rain_1h": "mean",
                 "snow_1h": "mean",
                 "clouds_all": "mean",
                 "weather_main": "first",
                 "weather_description": "first",
                 "traffic_volume": "mean"
             })
             .reset_index())
logger.info(f"Hourly dataset created: {len(hourly_df)} rows")

invalid_temp = (hourly_df["temp"] <= 0).sum()
logger.warning(f"Invalid temperature records: {invalid_temp}")

invalid_rain = (hourly_df["rain_1h"] > 9000).sum()
logger.warning(f"Extreme rainfall records: {invalid_rain}")

hourly_df.loc[
    hourly_df["temp"] <= 0, "temp"
] = pd.NA

hourly_df.loc[
    hourly_df["rain_1h"] > 9000, 
    "rain_1h"
] = pd.NA

temp_median = (
    hourly_df["temp"].
    median()
)

rain_median = (
    hourly_df["rain_1h"].
    median()
)

hourly_df["temp"] = (
    hourly_df["temp"]
    .fillna(temp_median)
)

hourly_df["rain_1h"] = (
          hourly_df["rain_1h"]
          .fillna(rain_median)
)

logger.warning(
    f"Replaced {invalid_temp} invalid temperature values using median ({temp_median:.2f})"
)

logger.warning(
    f"Replaced {invalid_rain} extreme rainfall values using median ({rain_median:.2f})"
)

hourly_df["weather_main"] = (
    hourly_df["weather_main"]
    .str.strip()
    .str.title()
)

hourly_df["weather_description"] = (
    hourly_df["weather_description"]
    .str.strip()
    .str.lower()
)

logger.info(
    "Standardized weather category values"
)

hourly_df.to_csv(
    "data/processed/traffic_clean.csv",
    index=False
)

logger.info(
    "Cleaned dataset saved to data/processed/traffic_clean.csv"
)

