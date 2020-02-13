from flask import escape, request
from app import app
from ..services import consultar_cidade


@app.route('/cidade', methods=['GET',])
def home_cidade():
    cidade = request.args.get('cidade')
    estado = request.args.get('cidade')
    dados = ''
    if estado is not None and cidade is not None:
        dados = consultar_cidade(cidade, estado)
    else:
        dados = "Nada deu certo!"
    return dados