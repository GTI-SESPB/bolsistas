from datetime import datetime

from flask import Blueprint, redirect, render_template, request, url_for
from flask.views import MethodView
from sqlalchemy import select, update, delete

from ..database import db
from ..models import Bolsista
from ..utils import class_route, dado_foi_deletado


bolsistas_bp = Blueprint('bolsistas', __name__)


@class_route(bolsistas_bp, '/bolsistas', 'listar')
class Listar(MethodView):
    def get(self):
        bolsistas = db.session.execute(select(Bolsista).where(Bolsista.data_deletado.is_(None))).scalars()
        return render_template('bolsistas/listar.html', bolsistas=bolsistas)


@class_route(bolsistas_bp, '/bolsistas/adicionar', 'adicionar')
class Adicionar(MethodView):
    def get(self):
        return render_template('bolsistas/adicionar.html')

    def post(self):
        form = dict(request.form)
        form['nascimento'] = datetime.strptime(form['nascimento'], '%Y-%m-%d')
        bolsista = Bolsista(**form)
        db.session.add(bolsista)
        db.session.commit()
        return redirect(url_for('bolsistas.visualizar', id=bolsista.id))


@class_route(bolsistas_bp, '/bolsistas/visualizar/<int:id>', 'visualizar')
class Visualizar(MethodView):
    def get(self, id: int):
        bolsista = db.session.execute(
            select(Bolsista).where(Bolsista.id == id)
        ).scalar()
        dado_foi_deletado(bolsista)
        return render_template('bolsistas/visualizar.html', bolsista=bolsista)


@class_route(bolsistas_bp, '/bolsistas/editar/<int:id>', 'editar')
class Editar(MethodView):
    def get(self, id: int):
        bolsista = db.session.execute(
            select(Bolsista).where(Bolsista.id == id)
        ).scalar()
        dado_foi_deletado(bolsista)
        return render_template('bolsistas/editar.html', bolsista=bolsista)

    def post(self, id: int):
        form = dict(request.form)
        form['nascimento'] = datetime.strptime(form['nascimento'], '%Y-%m-%d')
        dado_foi_deletado(db.session.execute(select(Bolsista).where(Bolsista.id == id)).scalar())       
        db.session.execute(update(Bolsista).where(Bolsista.id == id).values(**form))
        db.session.commit()
        return redirect(url_for('bolsistas.visualizar', id=form['id']))


@class_route(bolsistas_bp, '/bolsistas/deletar/<int:id>', 'deletar')
class Deletar(MethodView):
    def get(self, id: int):
        dado_foi_deletado(db.session.execute(select(Bolsista).where(Bolsista.id == id)).scalar())       
        db.session.execute(delete(Bolsista).where(Bolsista.id == id))
        db.session.commit()
        return redirect(url_for('bolsistas.listar'))


@class_route(bolsistas_bp, '/', 'home')
class Home(MethodView):
    def get(self):
        return redirect(url_for('bolsistas.listar'))
