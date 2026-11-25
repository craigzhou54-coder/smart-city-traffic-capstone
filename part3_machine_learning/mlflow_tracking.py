import mlflow

mlflow.set_experiment(
    "Traffic Volume Prediction"
)

# Random Forest
with mlflow.start_run():
    mlflow.log_param(
        "model",
        "RandomForestRegressor"
    )
    mlflow.log_metric(
        "MAE",
        390.75
    )
    mlflow.log_metric(
        "R2",
        0.899
    )

    print("MLflow run logged")

# Linear Regression
with mlflow.start_run(run_name="Linear Regression"):
    mlflow.log_param("model", "LinearRegression")
    mlflow.log_metric("MAE", 820.20)
    mlflow.log_metric("R2", 0.716)

# Neural Network
with mlflow.start_run(run_name="Neural Network"):
    mlflow.log_param("model", "MLPRegressor")
    mlflow.log_metric("MAE", 334.12)
    mlflow.log_metric("R2", 0.925)