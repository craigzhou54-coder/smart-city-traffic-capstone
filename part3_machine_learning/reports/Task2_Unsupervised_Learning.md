# K-Means Clustering
Three traffic clusters were identified using:
    Hour, Severe_Weather, Traffic_Volume

Cluster Summary:

Cluster Avg Hour Sever Weather Avg Traffic
0    3.14      0     933.57
1    14.96     0     4282.61
2    11.29     0     2999.52

Interpretation:

Cluster 0 represents low-traffic night-time periods.
Cluster 1 represents normal daytime high-demand conditions.
Cluster 2 represents observations occurring during severe weather conditions and may indicate weather-related disruption.

# Association Rule Mining
Association Rule Mining was performed using:

- Time Period
- Weekend Indicator
- Congestion Level
- Weather Conditions

A total of 17 frequent itemsets were identified.

## Rule 1
{Weekend, High_Congestion} -> {Afternoon}
Lift = 2.47

Interpretation:

Traffic observations that occur during weekends and high-congestion periods are approximately 2.47 times more likely to occur during the afternoon than expected by chance.

## Rule 2
{Afternoon} -> {High_Congestion}
Lift = 1.94

Interpretation:

Afternoon periods show a strong association with high congestion levels, indicating that traffic demand tends to be concentrated during daytime activity periods.

## Conclusion
The strongest association rules suggest that time-of-day factors are among the most important drivers of congestion levels.

Afternoon periods consistently appear in the highest-lift rules, indicating their importance in traffic management and congestion forecasting.