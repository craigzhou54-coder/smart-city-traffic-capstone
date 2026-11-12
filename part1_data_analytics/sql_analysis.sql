sqlite> select count(*) FROM traffic_data;
48204

qlite> select min(date_time), max(date_time)
   ...> from traffic_data;
2012-10-02 09:00:00|2018-09-30 23:00:00
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