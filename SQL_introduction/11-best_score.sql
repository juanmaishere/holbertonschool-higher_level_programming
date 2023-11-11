-- TOP SCORER - display order by top score where is plus than 10

-- Select columns and display ordered by score
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
