from .app import App
from .db import get_dbsession
from .models import User


@App.service('dbsession')
def dbsession_service(registry, settings):
    return get_dbsession(settings.sqlalchemy.__dict__)


class UsersService(object):
    def __init__(self, dbsession):
        self.dbsession = dbsession

    def all(self):
        return self.dbsession.query(User).all()

    def by_id(self, id):
        return self.dbsession.query(User)\
            .filter(User.id == id)\
            .first()

    def by_username(self, username):
        return self.dbsession.query(User)\
            .filter(User.username == username)\
            .first()

    def by_email(self, email):
        return self.dbsession.query(User)\
            .filter(User.email == email)\
            .first()


@App.service('users')
def users_service(registry, settings):
    dbsession = registry.find('dbsession')
    return UsersService(dbsession=dbsession)
