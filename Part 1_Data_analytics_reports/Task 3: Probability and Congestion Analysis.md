## 3.1 Basic probability
# Congestion Definition
Congestion is defined as traffic volume greater than 5,500 vehicle, as specified in the assignment brief.

Results:

Event                         Records                Probability
Congestion                    7,100                  0.1473(14.73)
Clear Weather                 13,391                 0.2778(27.78%)
Congestion and Clear Weather  1,763                  0.0366(3.66%)

Interpretation:
The probability of congestion is 14.73%, indicating that approximately one in seven hourly observations experienced traffic volumes exceeding 5,500 vehicles.
The probability of clear weather is 27.78%, meaning that slightly more than one quarter of observations were recorded under clear weather conditions.
The probability of congestion occurring during clear weather is 3.66%, suggesting that congestion and clear weather occur together relatively infrequently when considering all observations in the dataset.

## 3.2 Conditional probability
P(clear | congestion) = 1763/7100 = 0.2483
P(High Temperature | Congestion) = 1867/7100 = 0.2630
Interpretation
Amoung all congestion observations, 24.83% occurred during clear weather conditions.
Amoung all congestion observations, 29.58% occurred when temperatures exceeded 292K
The results suggest that congestion is not limited to adverse weather conditions and may occur under a variety of environmental conditions. Traffic demand and cmmuting patterns likely play a more important role than weather alone.

Determine whether weather conditions and congestion can be considered independent using P(A ∩ B) = P(A) × P(B)
P(Clear ∩ Congestion) = 1763/48204 = 0.0366
P(Clear) × P(Congestion) = 0.2777 × 0.1472 = 0.0409
Since 0.0366 ≠ 0.0409, weather conditions and congestion are not independent.

Calculate the odds ratio of congestion in clear versus cloudy weather. 

Weather Condition          Congestion          Non-Congestion          Odds
Clear                      1,763               11,628                  0.1516
Clouds                     2,592               12,572                  0.2062

Odds Ratio = 0.735
The odds ration of congestion in clear versus cloudy weather was 0.735.
An odds ratio below 1 indicates that congestion was less likely to occur during clear weather than during cloudy weatuer conditions.
This finding suggests that weather may have some association with congestion levels. However, the magnitude of the relationship appears relatively modest, indicating that traffic demand, commuting patterns, and time-of-day effects are likely to be more important factors influencing congestions.

### Conclusion:
The probability analysis suggests that weather conditions have some relationship with traffic congestions, but the effect appears relatively weak.

Congestion occurred in approximately 14.73% of observations, while clear weather was present in 27.78% of observations.

The independence test showed that congestion and clear weather are not completely independent events. In addition, the odds ratio of 0.735 indicates that congestion was less likely during clear weather than during cloudy weather.

Despite these findings, weather alone does not appear to be a strong determinant of congestion. Traffic patterns are likely influenced more strongly by factors such as commuting behaviour, peak-hour demand, weekdays versus weekends, and seasonal travel trends.