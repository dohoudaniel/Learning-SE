#!/usr/bin/python3

# PLD with Omar
from sqlalchemy import create_engine
import sys


user = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]

# The first () is for the user
# The second () is for the password
# The third () is for the database
db_url = "mysql+mysqldb://{}:{}@localhost/{}"
# Example: db_url = "mysql+mysqldb://root:password@localhost/my_database"
# In the example, user = root, password = password, and database = my_database
# Syntax: dialect+driver://username:password@hostname:port/database


engine = create_engine(db_url.format(user, password, database))
# engine.execute()  or  engine.connect()

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer(), primary_key=True)
    name = Column(String(50))
    fullname = Column(String(128))
    nickname = Column(String(128))

    def __repr__(self):
        return "<User(name='{}')>".format(self.name)

# Jottings
"""
sqlalchemy == core or orm === users = session.query(User).all()

connector / driver ==> mysql is mysqldb

Our database

from sqlalchemy import create_engine("res+dilect://{}:{}@localhost/databaseName")

database_sys = mysql
dialect(connector) = mysqldb
user = root
password = password
host = localhost
database_name
"""
