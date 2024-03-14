-- write a script that creates the table force_name on
-- 	your MySQL server.
-- don't fail if the table already exists.
CREATE TABLE IF NOT EXISTS force_name (
	id INT,
	name VARCHAR(256)
);
