-- create the database hbtn_0d_usa and the table states
-- 	states' id is INT, unique, auto-gen, can't be null,
--		is a primary key.
-- only do all this if not exists
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (
	id INT AUTO_INCREMENT PRIMARY KEY UNIQUE,
	name VARCHAR(256) NOT NULL
);
