from flask import Blueprint, render_template, request

from ..server import app
from ...models import Bolsistas


bolsistas_routes_bp = Blueprint('bolsistas_routes', __name__)


@bolsistas_routes_bp.get('/bolsistas')
def lista_bolsistas():
    pagina = app.db.paginate(app.db.select(Bolsistas))
    return render_template('bolsistas/listar.html', page=pagina)

@bolsistas_routes_bp.route('/bolsistas/adicionar', methods=['GET', 'POST'])
def adicionar_bolsista():
    if request.method == 'GET':
        return render_template('bolsistas/adicionar.html')

    bolsista = Bolsistas(**dict(request.form))
    app.db.session.add(bolsista)
    app.db.session.commit()
    return render_template('bolsistas/adicionar.html')


app.register_bp(bolsistas_routes_bp)
