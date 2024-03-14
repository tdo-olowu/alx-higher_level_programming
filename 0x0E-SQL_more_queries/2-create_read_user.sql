-- create the database hbtn_0d_2 and the user user_0d_2
-- give user only SELECT privilege in hbtn database
-- for both tasks, only do it if it doesn't already exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2';
GRANT SELECT ON hbtn_0d_2 TO 'user_0d_2';
