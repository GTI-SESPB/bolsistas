from flask import Blueprint, render_template
from flask.views import MethodView
from sqlalchemy import select

from ..database import db
from ..models import Bolsa
from ..utils import class_route


bolsas_bp = Blueprint('bolsas', __name__)


@class_route(bolsas_bp, '/bolsas', 'listar')
class Listar(MethodView):
    def get(self):
        bolsas = db.session.execute(select(Bolsa)).scalars()
        return render_template('bolsas/listar.html', bolsas=bolsas)

@class_route(bolsas_bp, '/bolsas/adicionar', 'adicionar')
class Adicionar(MethodView):
    def get(self):
        return render_template('bolsas/adicionar.html')
