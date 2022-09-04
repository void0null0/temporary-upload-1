from sqlalchemy import create_engine, Column, JSON, String, Integer
from sqlalchemy.orm import declarative_base, sessionmaker

base = declarative_base()
engine = create_engine('sqlite:///database.db', echo=True)
connection = engine.connect()
session = sessionmaker()

class Users(base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    cookie = Column(String, nullable=False)
    json = Column(JSON, nullable=False)

    def __init__(self, id, cookie, json):
        self.id = id
        self.cookie = cookie
        self.json = json

base.metadata.create_all(connection)