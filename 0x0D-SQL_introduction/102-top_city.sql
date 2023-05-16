---displays the average temp of 3 cities
-- during July and August
-- ordered by temperature desc

SELECT city, AVG(value) as avg_temp
FROM temperatures
WHERE month = "July" OR month = "August"
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
