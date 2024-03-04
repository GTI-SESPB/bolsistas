from flask import Blueprint, render_template

from ..server import app
from ...models import Bolsistas


bolsistas_routes_bp = Blueprint('bolsistas_routes', __name__)


@bolsistas_routes_bp.get('/bolsistas')
def lista_bolsistas():
    return render_template('bolsistas/listar.html')
