from pathlib import Path
from typing import Any

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy



class Server:
    def __init__(self) -> None:
        self.__app = Flask(
            __name__,
            template_folder=Path('./src/templates').absolute(),
            static_folder=Path('./src/static').absolute()
        )
        self.__app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
        self.__db = SQLAlchemy(self.__app)
        self.__migrate = Migrate(self.__app, self.__db)

        
    def register_bp(self, blueprint) -> None:
        self.__app.register_blueprint(blueprint)

    @property
    def db(self):
        return self.__db

    @property
    def migrate(self):
        return self.__migrate

    def __call__(self, *_: Any) -> Any:
        return self.__app


app = Server()
