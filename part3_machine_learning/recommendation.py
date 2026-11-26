import pandas as pd

df = pd.read_csv(
    "../part2_python/data/processed/traffic_features.csv")

hourly_traffic = (
    df.groupby("Hour")
    ["traffic_volume"]
    .mean()
    .sort_values()
)

low_hours = (
    hourly_traffic
    .head(3)
)

best_hours = (
    low_hours.index.tolist()
)

print(
    "\nTraffic Recommendation System"
)

print(
    f"Recommended low-traffic hours: {best_hours}"
)

best_hours = sorted(best_hours)

print(
    f"\nFor flexible journeys, consider travelling "
    f"between {best_hours[0]:02d}:00 and "
    f"{best_hours[-1]:02d}:59, "
    f"when historical traffic volumes are typically lower."
)

print(
    "\nAvoid peak congestion periods "
    "between 15:00-17:00."
)
