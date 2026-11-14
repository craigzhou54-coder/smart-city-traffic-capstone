# Part 1
# Task 1: SQL-Based Traffic Analysis
## 1.1 Load the dataset
    . Load the comma-delimited traffic CSV file into SQLite
    . Verify that the data has been loaded correctly

Load Result:
The dataset contains 48,204 traffic records.

Date Range:
2012-10-02 to 2018-09-30

2012-10|805
2012-11|785
2012-12|969
2013-01|706
2013-02|717
2013-03|715
2013-04|939
2013-05|940
2013-06|767
2013-07|748
2013-08|650
2013-09|478
2013-10|442
2013-11|590
2013-12|881
2014-01|787
2014-02|675
2014-03|738
2014-04|680
2014-05|778
2014-06|387
2014-07|658
2014-08|136
2015-06|186
2015-07|857
2015-08|860
2015-09|828
2015-10|571
2015-11|488
2015-12|583
2016-01|603
2016-02|616
2016-03|608
2016-04|775
2016-05|895
2016-06|741
2016-07|816
2016-08|826
2016-09|785
2016-10|727
2016-11|979
2016-12|935
2017-01|1026
2017-02|714
2017-03|865
2017-04|963
2017-05|952
2017-06|817
2017-07|850
2017-08|960
2017-09|805
2017-10|928
2017-11|844
2017-12|881
2018-01|884
2018-02|804
2018-03|867
2018-04|902
2018-05|871
2018-06|874
2018-07|866
2018-08|946
2018-09|935

## 1.2 Analysis annual traffic trends

Compare the total yearly traffic volume: 
2012|8208767
2013|28177412
2014|15731289
2015|14181206
2016|29494821
2017|35428156
2018|25914633

Year-on-Year Changes
Period                   Observation
2012->2013               Significant Increase
2013->2014               Substantial Decrease
2014->2015               Moderate Decrease
2015->2016               Strong Increase
2016->2017               Continued Increase
2017->2018               Decline Observed

Oberservations
1. Based on the available records, 2017 shows the highest total traffic volume.

2. Traffic totals appears substantially lower in 2014 and 2015.

3. These decreases should be interpreted with caution because the dataset contains a major gap between September 2014 and May 2015.

4. The dataset also contains partial years in 2012 (only Oct to Dec) and 2018 (only Jan to Sept), which makes direct year-to-year comparisons less reliable.

Data Quality Note: 
The annual traffic totals reported above reflect available observations rather than complete yearly traffic demand. Therefore, the results should be considered indicative rather than conclusive.

## 1.3 Analysis temperature around holidays
Labor Day
Year           Average Temperature(K)
2015            295.0
2016            293.2
2017            295.5

New Year's Day
Year           Average Temperature(K)
2015            N/A (250.1)
2016            265.9
2017            270.6

Obersvations
1. The assignment brief requires new year's Day temperatures for 2015, 2016 and 2017. However, no data exists for January 2015 due to a dataset gap between September 2014 and May 2015. To provide a three-year comparison, 2014 was used as the closest available historical observation.

2. Average temperature increased from 250.1K in 2014 to 265.9K in 2016 and further to 270.6K in 2017. This indicates progressively warmer New Year's Day conditions over the available observation period.

Traffic Impact Discussion
The available observations indicates that New Year's Day temperature increased between 2014 and 2017, while Labor Day temperatures remained comparatively stable. The warmer temperatures observed during New Year's Day in 2016 and 2017 may have supported improved travel conditions relative to the colder conditions recorded in 2014.
However, direct comparisons should be interpreted with caution because New Year's Day observations for 2015 are unavailable due to the dataset gap between September 2014 and May 2015.
Furthermore, traffic volume is influenced by multiple factors beyond temperature, including holiday travel behavior, weather events, and traffic demand patterns.
As a result, temperature differences may provide contextual insight into traffic conditions but cannot independently explain changes in traffic volume.

## 1.4 Data Quality Assessment
Several data quality issues were identified during the analysis.

1. Duplicate timestamps exist throughout the dataset.
2. A nine-month gap exists between September 2014 and May 2015.
3. Holiday indicators are recorded only at 00:00 rather than across an entire holiday
4. Several potentially invalid sensor reading were detected, including temperatures of 0 Kelvin and unusually high rainfall values.

These issues were documented and will be addressed during the data-cleaning process in Part 2.