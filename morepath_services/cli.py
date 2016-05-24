import click
import morepath
import transaction

from .app import App
from .models import(
    Base,
    User
    )


USERS = [{
    'username': 'john',
    'email': 'john@doe.com'
    }, {
    'username': 'jane',
    'email': 'jane@doe.com'
    }]


@click.command()
def initdb():
    click.echo('Initialize database...')
    morepath.autoscan()
    app = App()
    app.commit()
    # create database
    dbsession = app.find_service(name='dbsession')
    Base.metadata.create_all(dbsession.bind)
    # add users
    users = app.find_service(name='users')
    with transaction.manager:
        for user in USERS:
            users.add(**user)
        transaction.commit()


if __name__ == '__main__':
    initdb()
