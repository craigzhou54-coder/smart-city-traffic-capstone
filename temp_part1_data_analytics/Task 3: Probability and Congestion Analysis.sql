## 3.1 Basic probability
sqlite> select count(*)
   ...> from traffic_data
   ...> where traffic_volume > 5500;
7100
P(Congestion) = 7100/48204 = 0.1472


sqlite> select count(*)
   ...> from traffic_data
   ...> where weather_main='Clear';
13391
P(Clear) = 13391/48204 = 0.2777

sqlite> select count(*)
   ...> from traffic_data
   ...> where traffic_volume > 5500
   ...> and weather_main='Clear';
1763
P(Congestion and Clear) = 1763/48204 = 0.0366

## 3.2 Conditional probability
select count(*)
    ...> from traffic_data
    ...> where traffic_volume > 5500
    ...> and weather_main='Clear';
1763
P(clear | congestion) = 1763/7100 = 0.2483

Select count(*)
    ...> from traffic_data
    ...> where traffic_volume > 5500
    ...> and temp > 292;
    ...> 1867
P(High Temperature | Congestion) = 1867/7100 = 0.2630

Determine whether weather conditions and congestion 
can be considered independent using P(A ∩ B) = P(A) × P(B)

P(Clear ∩ Congestion) = 1763/48204 = 0.0366
P(Clear) × P(Congestion) = 0.2777 × 0.1472 = 0.0409

Since 0.0366 ≠ 0.0409, weather conditions and congestion are not independent.

Calculate the odds ratio of congestion in clear versus cloudy weather. 
sqlite> select count(*)
   ...> from traffic_data
   ...> where weather_main='Clouds';
15164

sqlite> select count(*)
   ...> from traffic_data
   ...> where weather_main='Clouds'
   ...> and traffic_volume > 5500;
2592

clear_odds = P(Congestion | Clear) / P(No Congestion | Clear) = 1763/(13391-1763) = 0.1516 
cloudy_odds = P(Congestion | Cloudy) / P(No Congestion | Cloudy) = 2592/(15164-2592) = 0.2062
odds_ratio = clear_odds / cloudy_odds = 0.1516 / 0.2062 = 0.7354
