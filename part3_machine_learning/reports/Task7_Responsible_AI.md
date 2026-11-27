## 1. Bias and Fairness Report

# Data Limitations and Coverage Issues

The traffic dataset contains several known limitations that may affect model performance and fairness.

A significant data gap exists between September 2014 and May 2015. In addition, the dataset begins in October 2012 and ends in September 2018, resulting in incomplete coverage for those years.

The dataset also contains duplicated timestamps and a small number of anomalous sensor readings, including invalid temperature values and extreme rainfall observations. These issues were identified and addressed during the data-cleaning stage.

# Proxy Labels and Associated Risks

Because no accident dataset was provided, a proxy label named High_Risk was created.

The label was generated using:

- High or Severe congestion conditions
- Severe weather conditions
- Low visibility conditions

This proxy does not represent actual accident occurrence.

The primary risk is that the model may learn patterns associated with congestion or adverse weather rather than genuine accident likelihood.

Therefore, predictions should be interpreted as estimated traffic risk rather than accident prediction.

# Uneven Error Distribution

Model performance may differ across:

- Daytime and night-time periods
- Weekdays and weekends
- Normal versus severe weather conditions

Because severe-weather observations and high-risk events are less common than normal traffic conditions, prediction errors may be higher within these minority scenarios.

Additional validation should therefore be performed before deploying the model in operational environments.

## 2. Governance and Sustainability

# Governance Requirements

Before any model is trusted for real-world decision-making, several governance controls should be implemented:

- Regular model validation and performance review
- Monitoring for prediction drift and feature drift
- Human oversight for critical operational decisions
- Documentation of model assumptions and limitations
- Periodic retraining using updated traffic data

Model recommendations should support human decision-makers rather than replace them.

# Sustainability Considerations

Different modelling approaches have different resource requirements.

Linear Regression required relatively little computational effort, while Neural Network training consumed more processing resources.

Although Neural Networks produced the strongest predictive performance, organisations should balance predictive accuracy against computational cost and energy consumption.

For many operational mobility applications, simpler models may offer adequate performance while consuming fewer resources and reducing environmental impact.

# Conclusion

The project demonstrates how machine-learning techniques can support mobility planning and traffic management. However, responsible deployment requires careful consideration of data quality, proxy-label limitations, fairness, governance procedures and sustainability trade-offs.