---displays the average temp of 3 cities
-- during July and August
-- ordered by temperature desc

SELECT city, value as avg_temp
FROM temperatures
WHERE month = 7 OR month = 8
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
