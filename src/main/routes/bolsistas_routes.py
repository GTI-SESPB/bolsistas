from datetime import datetime

from flask import Blueprint, redirect, render_template, request, url_for

from ..database import db
from ...models import Bolsistas


bolsistas_routes_bp = Blueprint('bolsistas_routes', __name__)


@bolsistas_routes_bp.get('/bolsistas')
def lista_bolsistas():
    bolsistas = db.session.execute(db.select(Bolsistas)).scalars()
    return render_template('bolsistas/listar.html', bolsistas=bolsistas)

@bolsistas_routes_bp.route('/bolsistas/adicionar', methods=['GET', 'POST'])
def adicionar_bolsista():
    if request.method == 'GET':
        return render_template('bolsistas/adicionar.html')

    form = dict(request.form)
    form['nascimento'] = datetime.strptime(form['nascimento'], '%Y-%m-%d')
    bolsista = Bolsistas(**form)
    db.session.add(bolsista)
    db.session.commit()
    return redirect(url_for('bolsistas_routes.lista_bolsistas'))

@bolsistas_routes_bp.route('/bolsistas/editar/<int:id>', methods=['GET', 'PUT'])
def editar(id: int):
    if request.method == 'GET':
        bolsista = db.session.execute(db.select(Bolsistas).where(Bolsistas.id == id)).scalar()
        return render_template('bolsistas/editar.html', bolsista=bolsista)

    form = dict(request.form)
    form['nascimento'] = datetime.strptime(form['nascimento'], '%Y-%m-%d')
    db.session.execute(
        db.update(Bolsistas).where(Bolsistas.id == id).valus(**form)
    )
    db.session.commit()
    return redirect(url_for('bolsistas_routes.lista_bolsistas'))

@bolsistas_routes_bp.get('/bolsistas/deletar/<int:id>')
def deletar(id: int):
    db.session.execute(
        db.delete(Bolsistas).where(Bolsistas.id == id)
    )
    db.session.commit()
    return redirect(url_for('bolsistas_routes.lista_bolsistas'))

@bolsistas_routes_bp.get('/')
def home():
    return redirect(url_for('bolsistas_routes.lista_bolsistas'))


