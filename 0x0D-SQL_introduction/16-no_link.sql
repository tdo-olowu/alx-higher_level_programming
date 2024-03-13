-- lists all records of the table second_table
-- does not list rows without a name value
-- displays the score and the name (in that order)
-- records listed by descending score
SELECT
	score,
	name
FROM
	second_table
WHERE
	name IS NOT NULL
ORDER BY
	score DESC;
