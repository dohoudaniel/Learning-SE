-- A script that loads and inserts values into a table
-- from  local text file.
-- The local text file used here is table_text_file.txt
LOAD DATA LOCAL INFILE './table_text_file.txt' INTO TABLE pet;
