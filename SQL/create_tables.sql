-- A script that creates a table in a MySQL database.
-- The database is passed as an argument to the SQL command.
-- The database being used here is the 'learning_sql' database.
CREATE TABLE pet (
	name VARCHAR(20),
	owner VARCHAR(20),
	specie VARCHAR(20),
	sex CHAR(1),
	birth DATE,
	death DATE
);
