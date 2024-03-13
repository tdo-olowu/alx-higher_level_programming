-- displays scores >= 10
-- lists scores from second_table
-- score and name, ordered from best to worst
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
