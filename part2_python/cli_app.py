import sys
import pandas as pd
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s")

logger = logging.getLogger(__name__)

df = pd.read_csv(
    "data/processed/traffic_features.csv")

if len(sys.argv) < 2:
    logger.error("No command provided")
    print(
        "Usage: python3 cli_app.py"
        "[peak|weekend|weather|recommend]")
    sys.exit()

command = sys.argv[1]

logger.info(
    f"Command invoked: {command}"
)

if command == "peak":
    peak_hour = (
        df.groupby("Hour")
        ["traffic_volume"]
        .mean()
        .idxmax()
    )
    peak_volume = (
        df.groupby("Hour")
        ["traffic_volume"]
        .mean()
        .max()
    )
    print(
        f"Peak Hour: {peak_hour}"
    )
    print(
        f"Average Traffic Volume: "
        f"{peak_volume:.0f}"
    )
elif command == "weekend":
    weekend_avg = (
        df.groupby("Weekend")
        ["traffic_volume"]
        .mean()
    )
    weekday_avg = weekend_avg[0]
    weekend_only_avg = weekend_avg[1]
    print(
        f"Weekday Average: {weekday_avg:.0f}")
    print(
        f"Weekend Average: {weekend_only_avg:.0f}"
    )
elif command == "weather":
    weather_avg = (
        df.groupby("weather_main")
        ["traffic_volume"]
        .mean()
    )
    top_weather = weather_avg.idxmax()
    top_volume = weather_avg.max()
    print(
        f"Top Weather Condition: {top_weather}")
    print(
        f"Average Traffic Volume: {top_volume:.0f}")

elif command == "recommend":
    low_hours = (
        df.groupby("Hour")
        ["traffic_volume"]
        .mean()
        .sort_values()
        .head(3)
    )
    print(
        "Recommended Travel Hours:")
    print(
        low_hours.index.tolist())
else:
    logger.error(
        f"Unknown command: {command}"
    )
    print(
        "Error: Unknown command."
    )
