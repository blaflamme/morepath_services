from more.transaction import TransactionApp
from more.services import ServiceApp


class App(TransactionApp, ServiceApp):
    pass


@App.setting_section(section='sqlalchemy')
def get_sqlalchemy_setting_section():
    return {
        'sqlalchemy.url': 'sqlite:///morepath_services.db'
        }
