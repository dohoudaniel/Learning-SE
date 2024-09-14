#!/usr/bin/python3

# Learning and practicing Python ORM
# Link: https://docs.sqlalchemy.org/en/13/orm/tutorial.html
# Using the Python interpreter

# Connecting
from sqlalchemy import create_engine
engine = create_engine('sqlite:///:memory:', echo=True)


# Declare a mapping
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
from sqlalchemy import Column, Integer, String
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)
    def __repr__(self):
       return "<User(name='%s', fullname='%s', nickname='%s')>" % (
                            self.name, self.fullname, self.nickname)

# Create a Schema
# User.__table__
Table('users', MetaData(bind=None),
            Column('id', Integer(), table=<users>, primary_key=True, nullable=False),
            Column('name', String(), table=<users>),
            Column('fullname', String(), table=<users>),
            Column('nickname', String(), table=<users>), schema=None)

# Creating a session
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
# In the case where your application does not yet have an Engine when you define your module-level objects, just set it up like this:
Session = sessionmaker()
# Later, when you create your engine with create_engine(), connect it to the Session using sessionmaker.configure():
Session.configure(bind=engine)  # once engine is available
