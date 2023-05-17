-- List records with score >= 10 from second_table

-- Records score >= 10 and order them in descending order
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
