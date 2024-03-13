-- create a named table in the current database,
--	if the table with that name doesn't already exist
-- don't use SHOW or SELECT
CREATE TABLE IF NOT EXISTS first_table (
	id INT,
	name VARCHAR(256)
	);
