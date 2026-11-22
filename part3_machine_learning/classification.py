import pandas as pd
from sklearn.model_selection import (train_test_split)
from sklearn.linear_model import (LogisticRegression)
from sklearn.ensemble import (RandomForestClassifier)
from sklearn.metrics import(
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score
)

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

y = df["High_Risk"]

X = df[features]

X_train, X_test, y_train, y_test = (
    train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )
)

# Logistic Regression

lr = LogisticRegression(
    max_iter=1000
)

lr.fit(
    X_train,
    y_train
)

lr_pred = lr.predict(X_test)

lr_prob = lr.predict_proba(X_test)[:,1]

print("\nLogistic Regression")

print(
    "Accuracy:",
    accuracy_score(
        y_test,
        lr_pred
    )
)

print(
    "Recall:",
    recall_score(
        y_test,
        lr_pred
    )
)

print(
    "F1:",
    f1_score(
        y_test,
        lr_pred
    )
)

print(
    "ROC AUC:",
    roc_auc_score(
        y_test,
        lr_prob
    )
)

# Random Forest Classifier

rf = RandomForestClassifier(
    random_state=42,
    n_estimators=100
)

rf.fit(
    X_train,
    y_train
)

rf_pred = rf.predict(X_test)

rf_prob = rf.predict_proba(X_test)[:,1]

print("\nRandom Forest Classifier")

print(
    "Accuracy:",
    accuracy_score(
        y_test,
        rf_pred
    )
)

print(
    "Precision:",
    precision_score(
        y_test,
        rf_pred
    )
)

print(
    "Recall:",
    recall_score(
        y_test,
        rf_pred
    )
)

print(
    "F1:",
    f1_score(
        y_test,
        rf_pred
    )
)

print(
    "ROC AUC:",
    roc_auc_score(
        y_test,
        rf_prob
    )
)
