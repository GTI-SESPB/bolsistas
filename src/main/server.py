from pathlib import Path

from flask import Flask
from flask_migrate import Migrate

from .database import db
from .routes import bolsistas_bp, bolsas_bp, editais_bp


app = Flask(
    __name__,
    template_folder=Path('./src/templates').absolute(),
    static_folder=Path('./src/static').absolute()
)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
db.init_app(app)

migrate = Migrate(app, db)


# registrando blueprints
app.register_blueprint(bolsistas_bp)
app.register_blueprint(bolsas_bp)
app.register_blueprint(editais_bp)
