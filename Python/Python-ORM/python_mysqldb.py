#!/usr/bin/python3
# A ChatGPT Python ORM Script - 24th August 2023
# A Python script created to understand how Python for MySQL works.
import MySQLdb    # Import MySQLdb
db = MySQLdb.connect(host=localhost, user=root, passwd=password, db=my_database)    # Establishing the connection
cur = db.cursor()    # Establishing the cursor, giving us the ability to have multiple seperate working environments through the same connection to the database.
cur.execute("CREATE DATABASE IF NOT EXISTS python_database")
cur.execute("CREATE TABLE IF NOT EXISTS first_table ( id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT, name VARCHAR(50) )")    # Creating an SQL Table
songs = ('2 Rocking Chairs', 'Hand Of God', 'Preoccupied', 'Meant To Live', 'While You Count Sheep')    # Inserting into the table
for song in songs:
    cur.execute("INSERT INTO song (title)  VALUES (%s)", song)
    print("Auto Increment ID: %s", cur.lastrowid)
    print("/n/nPrinting everything in the python_database database..../n")
    cur.execute("SELECT * FROM python_database")
# Close all cursors
cur.close()
# Close all databases
db.close()
