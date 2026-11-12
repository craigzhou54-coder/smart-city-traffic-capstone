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

