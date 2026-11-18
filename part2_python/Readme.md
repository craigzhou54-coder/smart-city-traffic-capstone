### Congestion Category Logic

A data-driven congestion category was created using traffic volume quartiles.

The traffic distribution was divided into four groups based on the 25th, 50th and 75th percentile thresholds:

- Low: traffic_volume < Q1
- Medium: Q1 <= traffic_volume <Q2
- High: Q2 <= traffic_volume < Q3
- Severe: traffic_volume >= Q3

This approach was selected because it reflects the actual distribution of traffic observations and provides balanced congestion classes for subsequent machine-learning tasks.

## Visualization Summary

### Traffic by Hour
Traffic volume peeks during afternoon commuting periods, with the highest 
average traffic occurring around 16:00

### Weekday vs Weekend
Weekday traffic volume is substantially higher than weekend traffic volume,
indicating strong commuter influence.

### Temperature vs Traffic
A week positive relationship exists between temperature and traffic volume, consistent with the observed correlation coefficient from Part 1.