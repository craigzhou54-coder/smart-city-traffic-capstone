## Task 2: Descriptive Statistics and Correlation
# 2.1 Traffic volume statistics
Result:
Statistic            Value
Mean                 3,259.82
Median               3,380
Standard Deviation   1,986.84
Variance             3,947,533.43
Minimum              0
Maximum              7,280
Range                7,280

Interpretation
The average hourly traffic volume was 3,259.82 vehicles. The median traffic volume was 3,380 vehicles, which is slightly higher than the mean. This suggests a mild left-skew in the distribution, possibly influenced by very low traffic observations and zero-volume records. 
The standard deviation of 1,986.84 and variance of approximately 3.95 million indicate substantial variability in traffic volume across observations.
Traffic volume ranged from 0 to 7,280 vehicles, producting a range of 7,280 vehicles. This wide range suggests that traffic conditions varied considerably throughout the dataset.
The presence of zero-volume observations may indicate unusual traffic conditions or potential data-quality issues identified during the exploratory analysis.

Data quality note:
Minimum traffic volume was recorded as 0 vehicles. While this may represent genuine low-traffic periods, it could also be influenced by sensor or recording anomalies previously identified in the dataset.

# 2.2 Correlation Analysis
Temperature vs Traffic volume: correlation coefficient(r) = 0.1303

Direction of Relationship:
The relationship between temperature and traffic volume is positive. As temperature increases, traffic volume tends to increase slightly.

Strength of the relationship:
The correlation coefficient between temperature and traffic volume is 0.1303. This indicates a very week positive relationship between the two variables. Although traffic volume tends to increase slightly as temperature rises, the strength of the relationship is week. Temperature alone is therefore not a strong predictor of traffic volume.
Other factors such as commuting patterns, time of day, weekdays versus weekends, holidays, and weather conditions are likely to have a great

Why correlation does not imply causation:
Correlation doesn not imply causation. Although temperature and traffic volume show a positive association, this does not prove that higher temperature directly cause increased traffic volume.
Both variables may be influenced by other factors. For example, warmer temperatures often occur during summer periods when travel activity is naturally higher. Similary, commuting schedules, public holidays, weather events, and seasonal patterns can affect traffic volume independently of temperature.
Therefore, the observed correlation should only be inerpreted an association rather than evidence of a causal relationship.