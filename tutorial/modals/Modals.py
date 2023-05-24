from sqlalchemy import Column, Integer, String
from tutorial import db

class User(db.Model):
    __tablename__ = 'user'

    userid = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    age = Column(Integer)
    email = Column(String, nullable=False)