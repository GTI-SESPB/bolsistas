from datetime import datetime

from flask import Blueprint, redirect, render_template, request, url_for
from flask.views import MethodView
from sqlalchemy import select, update

from ..database import db
from ..models import Bolsa, Edital
from ..utils import class_route, dado_foi_deletado


bolsas_bp = Blueprint('bolsas', __name__)


@class_route(bolsas_bp, '/bolsas', 'listar')
class Listar(MethodView):
    def get(self):
        bolsas = db.session.execute(select(Bolsa).where(Bolsa.data_deletado.is_(None))).scalars()
        return render_template('bolsas/listar.html', bolsas=bolsas)


@class_route(bolsas_bp, '/bolsas/adicionar', 'adicionar')
class Adicionar(MethodView):
    def get(self):
        editais = db.session.execute(select(Edital).where(Edital.data_deletado.is_(None))).scalars()
        return render_template('bolsas/adicionar.html', editais=editais)

    def post(self):
        bolsa = Bolsa(**request.form)
        db.session.add(bolsa)
        db.session.commit()
        return redirect(url_for('bolsas.listar'))


@class_route(bolsas_bp, '/bolsas/visualizar/<int:id>', 'visualizar')
class Visualizar(MethodView):
    def get(self, id: int):
        bolsa = db.session.execute(
            select(Bolsa).where(Bolsa.id == id)
        ).scalar()
        dado_foi_deletado(bolsa)
        return render_template('bolsas/visualizar.html', bolsa=bolsa)


@class_route(bolsas_bp, '/bolsas/editar/<int:id>', 'editar')
class Editar(MethodView):
    def get(self, id: int):
        bolsa = db.session.execute(
            select(Bolsa).where(Bolsa.id == id)
        ).scalar()
        dado_foi_deletado(bolsa)
        editais = db.session.execute(select(Edital).where(Edital.data_deletado.is_(None))).scalars()
        return render_template('bolsas/editar.html', editais=editais, bolsa=bolsa)

    def post(self, id: int):
        dado_foi_deletado(db.session.execute(select(Bolsa).where(Bolsa.id == id)).scalar())
        db.session.execute(update(Bolsa).where(Bolsa.id == id).values(**dict(request.form)))
        db.session.commit()
        return redirect(url_for('bolsas.visualizar', id=id))


@class_route(bolsas_bp, '/bolsas/deletar/<int:id>', 'deletar')
class Deletar(MethodView):
    def get(self, id: int):
        dado_foi_deletado(db.session.execute(select(Bolsa).where(Bolsa.id == id)).scalar())
        db.session.execute(
            update(Bolsa).where(Bolsa.id == id).values(data_deletado=datetime.utcnow())
        )
        db.session.commit()
        return redirect(url_for('bolsas.listar'))
