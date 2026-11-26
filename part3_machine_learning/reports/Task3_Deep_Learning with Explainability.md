## Neural Network for Demand Prediction
A neural net work (MLPRegressor) was trained to predict traffic volumes using engineered temporal, weather and traffic-related features.

Results:
MAE: 334.12
R²: 0.925

Interpretation:
The neural network achieved the strongest predictive performance among all evaluated regression models.

Compared with the Linear Regression model, prediction error was substantially reduced, while the R² score increased from 0.716 to 0.925.

The resultes indicate that complex non-linear relationships exist between traffic demand, time-based features and weather conditions. The neural network was more effective at learning these relationships that both Linear Regression and Random Forest models.

## Explainability (SHAP)
SHAP was applied to a Random Forest Regressor trained to predict traffic volume.

The SHAP summary plot indicates that temporal features are the most influential variable affecting traffic-volume predictions.

The most important predictors were:

1. Hour_Cos
2. Weekend
3. Hour
4. Hour_Sin

Weather-related variables such as Severe_Weather and Low_Visibility had smaller but measurable impacts.

Holiday_Flag contributed relatively little to prediction performance compared with temporal variables.

## Interpretation

The explainability results confirm findings from previous analyses. Traffic demands is driven primarily by time-related behavioural patterns, particularly commuting behaviour and daily traffic cycles.

Weather conditions influence traffic volume but play a secondary role relative to temporal features.