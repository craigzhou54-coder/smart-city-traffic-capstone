## Traffic volume statistics
sqlite> select
   ...> round(avg(traffic_volume),2)
   ...> as mean_traffic
   ...> from traffic_data;
3259.82

sqlite> select
   ...> min(traffic_volume) as min_traffic,
   ...> max(traffic_volume) as max_traffic,
   ...> max(traffic_volume)-min(traffic_volume) as range_traffic
   ...> from traffic_data;
0|7280|7280

sqlite> select traffic_volume
   ...> from traffic_data
   ...> order by traffic_volume
   ...> limit 1
   ...> offset (
(x1...> select count(*)/2
(x1...> from traffic_data);
3380

sqlite> select
   ...> avg(
(x1...> (traffic_volume - 
(x2...> (select avg(traffic_volume)
(x3...> from traffic_data)
(x2...> ) *
(x1...> (traffic_volume -
(x2...> (select avg(traffic_volume)
(x3...> from traffic_data)
(x2...> )
(x1...> ) as variance
   ...> from traffic_data;
3947533.42982987

sqlite> select
   ...> sqrt(
(x1...> avg(
(x2...> (traffic_volume -
(x3...> (select avg(traffic_volume)
(x4...> from traffic_data)
(x3...> ) *
(x2...> (traffic_volume -
(x3...> (select avg(traffic_volume)
(x4...> from traffic_data)
(x3...> )
(x2...> )
(x1...> ) as std_dev
   ...> from traffic_data;
1986.84006146189

