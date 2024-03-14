-- write a script that creates the table id_not_null on
-- 	your MySQL server.
-- give id a default of 1
-- don't fail if the table already exists.
CREATE TABLE IF NOT EXISTS id_not_null (
	id INT DEFAULT 1,
	name VARCHAR(256)
);
