from flask import escape, request
from app import app
from ..services import consultar_cidade


@app.route('/cidade', methods=['GET'])
def home_cidade():
    cidade = request.args.get('cidade')
    estado = request.args.get('estado')
    if estado is not None and cidade is not None:
        return consultar_cidade(cidade=cidade, estado=estado)
    else:
        return "Nada deu certo!"
