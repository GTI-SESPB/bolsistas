from flask import Blueprint, render_template, url_for, redirect
from flask.views import MethodView
from sqlalchemy import select

from ..database import db
from ..models import Edital
from ..utils import class_route


editais_bp = Blueprint('editais', __name__)


@class_route(editais_bp, '/editais', 'listar')
class Listar(MethodView):
    def get(self):
        editais = db.session.execute(select(Edital)).scalars()
        return render_template('editais/listar.html', editais=editais)

@class_route(editais_bp, '/editais/adicionar', 'adicionar')
class Adicionar(MethodView):
    def get(self):
        # return render_template('bolsas/adicionar.html')
        return redirect(url_for('bolsistas.listar'))
