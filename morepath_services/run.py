import morepath

from .app import App


def run():  # pragma: no cover
    morepath.autoscan()
    morepath.run(App())


def wsgi_factory():
    morepath.scan()
    morepath.commit()
    return App()


application = wsgi_factory()
