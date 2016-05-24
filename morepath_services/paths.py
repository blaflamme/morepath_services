from .app import App
from .models import (
    Root,
    Users,
    User
    )


@App.path(model=Root, path='/')
def get_root():
    return Root()


@App.path(model=Users, path='/users')
def get_users(request):
    service = request.app.find_service('users')
    users = service.all()
    return Users(users)


@App.path(
    model=User,
    path='/users/{id}',
    converters={'id': int}
    )
def get_user(request, id):
    service = request.app.find_service('users')
    return service.by_id(id=id)
