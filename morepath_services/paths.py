from .app import App
from .models import Root


@App.path(model=Root, path='/')
def get_root():
    return Root()
