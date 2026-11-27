import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s"
)

logger = logging.getLogger(__name__)

df = pd.read_csv(
    "../part2_python/data/processed/traffic_features.csv"
)

cluster_features = [
    "Hour",
    "Severe_Weather",
    "traffic_volume"
]

X = df[cluster_features]

scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)

kmeans = KMeans(
    n_clusters=3,
    random_state=42
)

df["Cluster"] = kmeans.fit_predict(X_scaled)

cluster_summary = (
    df.groupby("Cluster")
    [["Hour",
      "Severe_Weather",
      "traffic_volume"]]
    .mean()
)

print(cluster_summary)

