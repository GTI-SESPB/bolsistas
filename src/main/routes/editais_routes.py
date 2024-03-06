from datetime import datetime

from flask import Blueprint, render_template, url_for, redirect, request
from flask.views import MethodView
from sqlalchemy import select, update

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
        return render_template('editais/adicionar.html')

    def post(self):
        form = dict(request.form)
        form['data_assinatura'] = datetime.strptime(form['data_assinatura'], '%Y-%m-%d')
        edital = Edital(**form)
        db.session.add(edital)
        db.session.commit()
        return redirect(url_for('editais.visualizar', id=edital.id))

@class_route(editais_bp, '/editais/visualizar/<int:id>', 'visualizar')
class Visualizar(MethodView):
    def get(self, id: int):
        edital = db.session.execute(
            select(Edital).where(Edital.id == id)
        ).scalar()
        return render_template('editais/visualizar.html', edital=edital)


@class_route(editais_bp, '/editais/editar/<int:id>', 'editar')
class Editar(MethodView):
    def get(self, id: int):
        edital = db.session.execute(
            select(Edital).where(Edital.id == id)
        ).scalar()
        return render_template('editais/editar.html', edital=edital)

    def post(self, id: int):
        form = dict(request.form)
        form['data_assinatura'] = datetime.strptime(form['data_assinatura'], '%Y-%m-%d')
        db.session.execute(update(Edital).where(Edital.id == id).values(**form))
        db.session.commit()
        return redirect(url_for('editais.visualizar', id=id))
