# A simple ChatGPT to play with SQLAlchemy!
#!/usr/bin/pythontablishing a connection
from sqlalchemy import create_engine
# engine = create_engine("mysql:///my_python_database.db")

# Using SQLAlchemy core
# Define tables
from sqlalchemy import Table, Column, Integer, String, MetaData
metadata = MetaData()
users = Table('users', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('age', Integer)
)
# Create tables in the database
metadata.create_all(engine)

# Using SQLAlchemy ORM
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

# Interact with the database using sessions
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()
new_user = User(name='Daniel', age=20)
session.add(new_user)
session.commit()

# Establishing a connection
from sqlalchemy import create_engine
engine = create_engine('mysql://my_python_database.db')

# Using SQLAlchemy core
# Define tables
from sqlalchemy import Table, Column, Integer, String, MetaData
metadata = MetaData()
users = Table('users', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('age', Integer)
)
# Create tables in the database
metadata.create_all(engine)

# Using SQLAlchemy ORM
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

# Interact with the database using sessions
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()
new_user = User(name='Daniel', age=20)
session.add(new_user)
session.commit()
