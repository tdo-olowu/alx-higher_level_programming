-- create database hbtn_0d_usa and table cities
-- cities has following parameters:
--	id is INT, unique, autogen, can't be null, is primary key
--	state_id is INT, NOT NULL, FOREIGN KEY which
--		references id of states table
--	name is VARCHAR(256) can't be null
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (
	id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
	state_id INT NOT NULL,
	name VARCHAR(256) NOT NULL,
	FOREIGN KEY (state_id) REFERENCES states(id)
);
