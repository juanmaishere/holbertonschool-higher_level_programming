-- SUBQUERY SELECT ALL RESULTS WITH X

-- Select all cities in California and order by cities.id
SELECT cities.id, cities.name
FROM cities
WHERE state_id = (
    SELECT id FROM states
    WHERE name = "California"
)
ORDER BY cities.id ASC;
