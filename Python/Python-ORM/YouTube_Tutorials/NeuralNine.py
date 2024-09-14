#!/usr/bin/python3

# Link: https://www.youtube.com/watch?v=AKQ3XEDI9Mw
# (SQLAlchemy Tutorial | Python ORM Example | Python Certification Training | Edureka)
import sys
import sqlalchemy
from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Person(Base):
    __tablename__ = "people"

    sn = Column("ssn", Integer, primary_key=True)
    firstname = Column("firstname", String(50))
    lastname = Column("lastname", String(50))
    gender = Column("gender", CHAR)
    age = Column("age", Integer)

    def __init__(self, sn, firstname, lastname, gender, age):
        self.sn = sn
        self.firstname = firstname
        self.lastname = lastname
        self.gender = gender
        self.age = age

    def __repr__(self):
        return "{} {} {} {} {}".format(self.sn, self.firstname, self.lastname, self.gender, self.age)


# Imagine we have a database named my_database
engine = create_engine("mysql+mysqldb://root:password@localhost:3306/learning_sqlalchemy", echo=True)
Base.metadata.create_all(bind=engine)   # This creates the Person table
Session = sessionmaker(bind=engine)
session = Session()

# Creating a new person
person = Person(1, "Daniel", "Dohou", "M", 20)
# Adding the person to the session
session.add(person)
# Committing the person to the session
session.commit()

# Returning everything from our Person table
results = session.query(Person).all()
print(results)
