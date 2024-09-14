#!/usr/bin/python3

# Link: https://docs.sqlalchemy.org/en/13/core/engines.html#database-urls


""" Engine configuration """
# Using Python3
# Connector / Driver: mysqldb
from sqlalchemy import create_engine
# Syntax: dialect+driver://username:password@host:port/database
engine = create_engine("mysql+mysqldb://root:password@localhost:3306/my_database")


""" Working with engines and connections """
with engine.connect() as execution:
    result = connection.execute("SELECT username FROM users")
    for row in result:
        print("username: ", row["username"])
