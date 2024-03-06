from flask import Blueprint, redirect, render_template, request, url_for
from flask.views import MethodView
from sqlalchemy import select

from ..database import db
from ..models import Bolsa, Edital
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
        editais = db.session.execute(select(Edital)).scalars()
        print(editais)
        return render_template('bolsas/adicionar.html', editais=editais)

    def post(self):
        bolsa = Bolsa(**request.form)
        db.session.add(bolsa)
        db.session.commit()
        return redirect(url_for('bolsas.listar'))

@class_route(bolsas_bp, '/bolsas/visualizar/<int:id>', 'visualizar')
class visualizar(MethodView):
    def get(self, id: int):
        bolsa = db.session.execute(
            select(Bolsa).where(Bolsa.id == id)
        ).scalar()
        return render_template('bolsas/visualizar.html', bolsa=bolsa)
