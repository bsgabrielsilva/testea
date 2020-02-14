from flask import request, jsonify, make_response

from app import app
from ..services import consultar_cidade
from ..db_services import cadastrar_cidade, listar_cidade_id
from ..entity import CidadeEntity
from ..schemas import CidadeSchema
import json


@app.route('/cidade/consultar', methods=['GET'])
def home_cidade():
    cidade = request.args.get('cidade')
    estado = request.args.get('estado')
    if estado is not None and cidade is not None:
        dados = consultar_cidade(cidade=cidade, estado=estado)
        if dados is not None:
            check = listar_cidade_id(dados['id'])
            cidade_schema = CidadeSchema()
            if check is None:
                cd = CidadeEntity(id=dados['id'], nome=dados['name'], estado=dados['state'], pais=dados['country'])
                dt = cadastrar_cidade(cd)
                return make_response(cidade_schema.jsonify(dt), 200)
            else:
                return make_response(cidade_schema.jsonify(check), 200)
        else:
            return make_response({'message': 'Algo de errado na solicitação! A consulta não retornou dados!'}, 404)
    elif estado is None and cidade is not None:
        return make_response({'message': 'Estado é necessário! Adicione &estado=UF'}, 400)
    elif cidade is None and estado is not None:
        return make_response({'message': 'Cidade é necessário! Adicione &cidade=Nome'}, 400)
    else:
        return make_response({'message': 'Algo deu errado na solicitação!'}, 400)
