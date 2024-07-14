-- Display average temprature
SELECT city, AVG(temperature) AS average_temperature
FROM your_table_name
GROUP BY city
ORDER BY average_temperature DESC;
