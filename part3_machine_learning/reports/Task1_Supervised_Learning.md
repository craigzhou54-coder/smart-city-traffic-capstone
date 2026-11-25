# Task 1: Supervised Learning Models
## Regression

Model	                MAE	    R²
Linear Regression	    820.20	0.716
Random Forest Regressor	390.75	0.899

### Findings

The Random Forest Regressor outperformed the Linear Regression models across both evaluation metrics.

The Random Forest model reduced the prediction error from approximately 820 vehicles to approximately 391 vehicles and achieved an R^2 value of 0.899.

This indicates that traffic volume is influenced by non-linear relationships which are captured more effectively by a three-based models.

## Classification

Model	                  Accuracy	 Precision	 Recall	    F1	      ROC AUC
Logistic Regression	      0.9847	 ...	     0.8870	    0.8946	  0.9963
Random Forest Classifier  0.9853	 0.9003	     0.8988	    0.8996	  0.9931

### Findings
Both classification models achieved excellent predictive performance.

Random Forest produced slightly better Accuracy, Precision, Recall and F1-score, While Logistics Regression achieved a marginally higher ROC AUC.

Overall, Random Forest was selected as the preferred classification model due to its stronger performance across most evaluation metrics.