-- SUBQUERY SELECT ALL RESULTS WITH X

SELECT id FROM states
WHERE name = "California";

-- Select all cities in California and order by id
SELECT name FROM cities
WHERE state_id = (
    SELECT id FROM states
    WHERE name = "California"
)
ORDER BY id ASC;
