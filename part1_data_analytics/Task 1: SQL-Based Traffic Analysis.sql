## load data validation
sqlite> select count(*) FROM traffic_data;
48204

sqlite> select
   ...> strftime('%Y-%m', date_time) as month,
   ...> count(*) as records
   ...> from traffic_data
   ...> group by month
   ...> order by month;
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

qlite> select min(date_time), max(date_time)
   ...> from traffic_data;
2012-10-02 09:00:00|2018-09-30 23:00:00



## Yearly Analysis
sqlite> select> select 
   ...> strftime('%Y', date_time) as year,
   ...> sum(traffic_volume) as total_traffic
   ...> from traffic_data
   ...> group by year
   ...> order by year;
2012|8208767
2013|28177412
2014|15731289
2015|14181206
2016|29494821
2017|35428156
2018|25914633

## New Years Day and Labor Day Temperature Analysis
sqlite> select
   ...> holiday,
   ...> strftime('%Y', date_time) as year,
   ...> round(avg(temp),1) as avg_temp
   ...> from traffic_data
   ...> where holiday in ('New Years Day', 'Labor Day')
   ...> group by holiday, year
   ...> order by holiday, year;
Labor Day|2013|288.8
Labor Day|2015|295.0
Labor Day|2016|293.2
Labor Day|2017|295.5
Labor Day|2018|292.4
New Years Day|2013|263.5
New Years Day|2014|250.1
New Years Day|2016|265.9
New Years Day|2017|270.6
New Years Day|2018|249.4

## Weather Analysis
sqlite> select
   ...> weather_main,
   ...> round(avg(traffic_volume),0) as avg_traffic
   ...> from traffic_data
   ...> group by weather_main
   ...> order by avg_traffic DESC;
Clouds|3618.0
Haze|3502.0
Rain|3318.0
Drizzle|3291.0
Smoke|3238.0
Clear|3056.0
Snow|3017.0
Thunderstorm|3002.0
Mist|2933.0
Fog|2704.0
Squall|2062.0

## Yearly Analysis
sqlite> select 
   ...> strftime('%Y', date_time) as year,
   ...> round(avg(traffic_volume),0) as avg_traffic
   ...> from traffic_data
   ...> group by year;
2012|3208.0
2013|3287.0
2014|3251.0
2015|3243.0
2016|3169.0
2017|3341.0
2018|3260.0

## Peak Hour Analysis
sqlite> select
   ...> strftime('%H', date_time) as hour,
   ...> Round(AVG(traffic_volume),0) as avg_traffic
   ...> from traffic_data
   ...> group by hour
   ...> order by hour;
00|835.0
01|516.0
02|388.0
03|371.0
04|703.0
05|2095.0
06|4141.0
07|4740.0
08|4587.0
09|4385.0
10|4185.0
11|4466.0
12|4718.0
13|4715.0
14|4932.0
15|5241.0
16|5664.0
17|5310.0
18|4264.0
19|3276.0
20|2835.0
21|2669.0
22|2199.0
23|1469.0

## Weekend vs Weekday Analysis
sqlite> select 
   ...> case
   ...> when strftime('%w', date_time) in ('0', '6')
   ...> then 'Weekend'
   ...> else 'Weekday'
   ...> End as day_type,
   ...> Round(AVG(traffic_volume),0) as avg_traffic
   ...> from traffic_data
   ...> group by day_type;
Weekday|3534.0
Weekend|2571.0

## Holiday Analysis
sqlite> select holiday,
   ...> round(avg(traffic_volume),0) as avg_traffic,
   ...> count(*) as records
   ...> from traffic_data
   ...> where holiday is not null
   ...> group by holiday
   ...> order by avg_traffic DESC;
New Years Day|1356.0|6
Memorial Day|1108.0|5
Independence Day|1076.0|5
Labor Day|1013.0|7
Thanksgiving Day|934.0|6
Christmas Day|828.0|6
Veterans Day|691.0|5
Washingtons Birthday|635.0|5
State Fair|635.0|5
Martin Luther King Jr Day|613.0|6
Columbus Day|519.0|5

## Monthly Analysis
sqlite> select strftime('%m', date_time) as month,
   ...> round(avg(traffic_volume),0) as avg_traffic
   ...> from traffic_data
   ...> group by month
   ...> order by month;
01|3051.0
02|3198.0
03|3308.0
04|3304.0
05|3366.0
06|3419.0
07|3205.0
08|3394.0
09|3303.0
10|3391.0
11|3168.0
12|3024.0

## Temperature Analysis
sqlite> select round(temp) as temperature,
   ...> round(avg(traffic_volume),0) as avg_traffic
   ...> from traffic_data
   ...> group by round(temp)
   ...> order by temperature;
0.0|1318.0
243.0|1462.0
244.0|919.0
245.0|477.0
246.0|2052.0
247.0|1822.0
248.0|2431.0
249.0|2493.0
250.0|2490.0
251.0|2357.0
252.0|3035.0
253.0|2592.0
254.0|2735.0
255.0|3023.0
256.0|3163.0
257.0|2893.0
258.0|3081.0
259.0|2880.0
260.0|2835.0
261.0|2876.0
262.0|3135.0
263.0|2895.0
264.0|2886.0
265.0|3031.0
266.0|3137.0
267.0|3133.0
268.0|2980.0
269.0|2955.0
270.0|3038.0
271.0|2992.0
272.0|2901.0
273.0|3163.0
274.0|3191.0
275.0|3201.0
276.0|3405.0
277.0|3408.0
278.0|3297.0
279.0|3225.0
280.0|3149.0
281.0|3236.0
282.0|3259.0
283.0|3196.0
284.0|3392.0
285.0|3110.0
286.0|3188.0
287.0|3204.0
288.0|3107.0
289.0|3033.0
290.0|3112.0
291.0|3085.0
292.0|3109.0
293.0|3190.0
294.0|3332.0
295.0|3412.0
296.0|3549.0
297.0|3668.0
298.0|3970.0
299.0|4282.0
300.0|4403.0
301.0|4531.0
302.0|4661.0
303.0|4593.0
304.0|4637.0
305.0|4876.0
306.0|5088.0
307.0|4965.0
308.0|4932.0
309.0|4957.0
310.0|3810.0

## Temperature Analysis for Holidays
sqlite> select
   ...> holiday,
   ...> strftime('%Y', date_time) as year,
   ...> round(avg(temp),1) as avg_temp
   ...> from traffic_data
   ...> where holiday in ('New Years Day', 'Labor Day')
   ...> group by holiday, year
   ...> order by holiday, year;
Labor Day|2013|288.8
Labor Day|2015|295.0
Labor Day|2016|293.2
Labor Day|2017|295.5
Labor Day|2018|292.4
New Years Day|2013|263.5
New Years Day|2014|250.1
New Years Day|2016|265.9
New Years Day|2017|270.6
New Years Day|2018|249.4