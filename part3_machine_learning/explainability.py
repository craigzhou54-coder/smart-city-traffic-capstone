import pandas as pd
import shap
import matplotlib.pyplot as plt
from sklearn.ensemble import(
    RandomForestRegressor
)
from sklearn.model_selection import(
    train_test_split
)

# Read data
df = pd.read_csv(
    "../part2_python/data/processed/traffic_features.csv"
)

print("Step 1")

# Feature Set
features = [
    "Hour",
    "Weekend",
    "Hour_Sin",
    "Hour_Cos",
    "Severe_Weather",
    "Low_Visibility",
    "Holiday_Flag",
    "Temp_Scales"
]

# Target
X = df[features]
y = df["traffic_volume"]

# Train Test Split
X_train, X_test, y_train, y_test = (
    train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )
)

# Random Forest
rf = RandomForestRegressor(
    random_state=42,
    n_estimators=100
)

rf.fit(
    X_train,
    y_train
)

print("Step 2")

# SHAP
explainer = shap.TreeExplainer(
    rf
)
# shap_values = explainer.shap_values(
#    X_test
#)

X_sample = X_test.sample(
    n=500,
    random_state=42
)

shap_values = explainer.shap_values(
    X_sample
)

print("Step 3")

# Summary Plot
#shap.summary_plot(
#    shap_values,
#    X_test,
#    show=False
#)

shap.summary_plot(
    shap_values,
    X_sample,
    show=False
)

plt.savefig(
    "./figures/shap_summary.png",
    bbox_inches="tight"
)

print("Step 4")

plt.close()
