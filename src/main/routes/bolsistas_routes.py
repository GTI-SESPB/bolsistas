from datetime import datetime

from flask import Blueprint, redirect, render_template, request, url_for
from flask.views import MethodView
from sqlalchemy import select, update, delete

from ..database import db
from ...models import Bolsistas
from ..utils import class_route


bolsistas_bp = Blueprint('bolsistas', __name__)


@class_route(bolsistas_bp, '/bolsistas', 'listar')
class Listar(MethodView):
    def get(self):
        bolsistas = db.session.execute(select(Bolsistas)).scalars()
        return render_template('bolsistas/listar.html', bolsistas=bolsistas)


@class_route(bolsistas_bp, '/bolsistas/adicionar', 'adicionar')
class Adicionar(MethodView):
    def get(self):
        return render_template('bolsistas/adicionar.html')

    def post(self):
        form = dict(request.form)
        form['nascimento'] = datetime.strptime(form['nascimento'], '%Y-%m-%d')
        bolsista = Bolsistas(**form)
        db.session.add(bolsista)
        db.session.commit()
        return redirect(url_for('bolsistas.listar'))


@class_route(bolsistas_bp, '/bolsistas/editar/<int:id>', 'editar')
class Editar(MethodView):
    def get(self, id: int):
        bolsista = db.session.execute(
            select(Bolsistas).where(Bolsistas.id == id)
        ).scalar()
        return render_template('bolsistas/editar.html', bolsista=bolsista)

    def put(self, id: int):
        form = dict(request.form)
        form['nascimento'] = datetime.strptime(form['nascimento'], '%Y-%m-%d')
        db.session.execute(update(Bolsistas).where(Bolsistas.id == id).values(**form))
        db.session.commit()
        return redirect(url_for('bolsistas.listar'))


@class_route(bolsistas_bp, '/bolsistas/deletar/<int:id>', 'deletar')
class Deletar(MethodView):
    def delete(self, id: int):
        db.session.execute(delete(Bolsistas).where(Bolsistas.id == id))
        db.session.commit()
        return redirect(url_for('bolsistas.listar'))


@class_route(bolsistas_bp, '/', 'home')
class Home(MethodView):
    def get(self):
        return redirect(url_for('bolsistas.listar'))
