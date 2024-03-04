from .main.server import app as app
from .models import *


def application():
    return app()
