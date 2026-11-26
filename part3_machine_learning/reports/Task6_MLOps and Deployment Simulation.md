## 6.1 Model Versioning

Version.               Model                MAE                R²
V1                Linear Regression        820.20            0.716
V2             Random Forest Regressor     390.75            0.899
V3                 Neural Network          334.12            0.925

Conclusion
Model performance improved progressively across version.
The Neural Network achieved lowest prediction error and the highest R² score.

## 6.2 Experiment Tracking
MLflow was used to track
    .Parameters
    .Metrics
    .Model versions
    .Experiment runs

## 6.3 Deployment - FastAPI
A FastAPI deployment mock-up was created to simulate production deployment.

Endpoint:

/predict

Input:

- hour:
- weekend

Output:

- predicted_traffic

Example:
{
    "hour": 16,
    "predicted_traffic": 3500
}

This demostrates how the traffic prediction model could be exposed through a REST API and consumed by external application.

## 6.4 Monitoring
prediction-error drift monitoring was simulated using Mean Absolute Error (MAE)

Baselie MAE:
390.76

current MAE:
520.00

Error Drift:
33.8%

The increase in prediction error suggests that models preformance has deteriorated relavite to the baseline model.

This may indicate data drive, concept drift, or changing traffic patterns.

## 6.5 Alerting
The simulated monitoring process detected a 72.90% increase in prediction error relative to the baseline model.

Because the observed error drift exceeded the predefined threshold of 20%, the system generated:

ALERT / Requires Investigation

This alert may indicate concept drift, data drift, or change is traffic behaviour that justify model retraining.