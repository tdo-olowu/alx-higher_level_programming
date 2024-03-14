-- write a script that creates the table unique_id on
-- 	your MySQL server.
-- give id default of 1, and make sure it is unique.
-- don't fail if the table already exists.
CREATE TABLE IF NOT EXISTS id_not_null (
	id INT DEFAULT 1,
	name VARCHAR(256),
	UNIQUE (id)
);
