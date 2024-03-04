from pathlib import Path

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from ..routes import bolsistas_routes_bp


app = Flask(__name__, template_folder=Path('./src/templates').absolute())
app.register_blueprint(bolsistas_routes_bp)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
db = SQLAlchemy(app)
migrate = Migrate(app, db)
