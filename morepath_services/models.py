from sqlalchemy import (
    Column,
    Integer,
    Text
    )
from .db import Base


class Root(object):
    pass


class Users(object):
    def __init__(self, users):
        self.users = users


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(Text)
    email = Column(Text)
