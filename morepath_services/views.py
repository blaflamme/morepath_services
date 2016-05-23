from .app import App
from .models import Root


@App.json(model=Root)
def root_view(self, request):
    return {'name': 'root'}
