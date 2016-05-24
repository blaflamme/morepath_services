from .app import App
from .models import (
    Root,
    Users,
    User
    )


@App.json(model=Root)
def root_view(self, request):
    return {'name': 'root'}


@App.json(model=Users)
def users_view(self, request):
    return {
        'users': [request.view(user) for user in self.users]
        }


@App.json(model=User)
def user_view(self, request):
    return {
        'username': self.username,
        'email': self.email
        }
