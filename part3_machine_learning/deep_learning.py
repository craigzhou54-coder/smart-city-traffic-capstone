# Import Data
import pandas as pd
from sklearn.model_selection import(
    train_test_split
)
from sklearn.metrics import (
    mean_absolute_error,
    r2_score
)
from sklearn.neural_network import (
    MLPRegressor
)

# Read Data
df = pd.read_csv(
    "../part2_python/data/processed/traffic_features.csv"
)

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

# Neural Network
nn = MLPRegressor(
    hidden_layer_sizes=(64,32),
    max_iter=500,
    random_state=42
)

nn.fit(
    X_train,
    y_train
)

# Evaluation
nn_pred = nn.predict(X_test)
print("\nNeural Network")
print(
    "MAE:",
    mean_absolute_error(
        y_test,
        nn_pred
    )
)

print(
    "R2:", 
    r2_score(
        y_test,
        nn_pred
    )
)