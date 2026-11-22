import pandas as pd
from sklearn.model_selection import (train_test_split)
from sklearn.linear_model import (LinearRegression)
from sklearn.ensemble import (RandomForestRegressor)
from sklearn.metrics import (mean_absolute_error, r2_score)

df = pd.read_csv("../part2_python/data/processed/traffic_features.csv")

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

X = df[features]

y = df["traffic_volume"]

X_train, X_test, y_train, y_test = (
    train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )
)

#Linear Regression

lr = LinearRegression()

lr.fit(X_train, y_train)

lr_pred = lr.predict(X_test)

print("\nLiner Regression")

print(
    "MAE:",
    mean_absolute_error(
        y_test,
        lr_pred
    )
)

print(
    "R2:",
    r2_score(
        y_test,
        lr_pred
    )
)

# Random Forest Regression

rf = RandomForestRegressor(
    random_state=42,
    n_estimators=100
)

rf.fit(X_train, y_train)

rf_pred = rf.predict(X_test)

print("\nRandom Forest")

print(
    "MAE:",
    mean_absolute_error(
        y_test,
        rf_pred
    )
)

print(
    "R2:",
    r2_score(
        y_test,
        rf_pred
    )
)

print(df["High_Risk"].value_counts())
