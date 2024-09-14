# A ChatGPTPython script that sets up mysql.connector
#!/usr/bin/python3
from mysql.connector import connection

mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password"
)
print(mydb)

