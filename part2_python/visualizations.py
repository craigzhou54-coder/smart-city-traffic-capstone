# Task 3: Visualise Traffic Patterns
# Visualization 1 - Traffic Demand by Hour

import pandas as pd
import matplotlib.pyplot as plt
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)
logger = logging.getLogger(__name__)

df = pd.read_csv(
    "data/processed/traffic_features.csv"
)

hourly = (
    df.groupby("Hour")
    ["traffic_volume"]
    .mean()
)

plt.figure(figsize=(10, 5))
hourly.plot()

plt.title(
    "Average Traffic Volume by Hour"
)

plt.xlabel("Hour")
plt.ylabel("Traffic Volume")

plt.xlabel("Hour")
plt.ylabel("Traffic Volume")

plt.savefig(
    "figures/traffic_by_hour.png"
)

plt.close()

logger.info(
    "Saved figures/traffic_by_hour.png"
)

#Visualization 2 - Weekday vs Weekend
weekend = (
    df.groupby("Weekend")
    ["traffic_volume"]
    .mean()
)

plt.figure(figsize=(6, 4))
weekend.plot(kind="bar")

plt.title("Weekday vs Weekend Traffic")

plt.savefig("figures/weekday_weekend.png")

logger.info("Saved figures/weekday_weedkend.png")

# Visuallization 3
plt.figure(figsize=(8, 5))

plt.scatter(
    df["temp"],
    df["traffic_volume"],
    alpha=0.2
)

plt.title(
    "Temerature vs Traffic Voklume"
)

plt.xlabel("Temperature")
plt.ylabel("Traffic Volume")

plt.savefig("figures/temperature_traffic.png")

logger.info(
    "Saved figures/temperature_traffic.png"
)

