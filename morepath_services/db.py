from sqlalchemy import engine_from_config
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from zope.sqlalchemy import register


Base = declarative_base()


def get_dbsession(settings):
    engine = engine_from_config(settings)
    maker = sessionmaker()
    maker.configure(bind=engine)
    session = maker()
    register(session)
    return session
