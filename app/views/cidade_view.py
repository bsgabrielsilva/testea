from flask import request, jsonify, make_response

from app import app
from ..services import consultar_cidade, consultar_cidade_id, consultar_tempo
from ..db_services import cadastrar_cidade, listar_cidade_id, cadastrar_tempo, listar_tempo_id, listar_tempo_data_cidade
from ..entity import CidadeEntity, TempoEntity
from ..schemas import CidadeSchema
from ..utils import tratamento_tempo, checar_tempo


@app.route('/cidade/cadastrar', methods=['GET'])
def cadastro_cidade():
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


@app.route('/cidade', methods=['GET'])
def home_cidade():
    id = request.args.get('id')
    cidade = listar_cidade_id(id)
    cidade_schema = CidadeSchema()
    if cidade is not None:
        obj = checar_tempo(id=id, cidade=cidade, schema=cidade_schema)
        return obj
    else:
        dd = consultar_cidade_id(cidade_id=id)
        if dd is not None:
            check = listar_cidade_id(dd['id'])
            if check is None:
                cd = CidadeEntity(id=dd['id'], nome=dd['name'], estado=dd['state'], pais=dd['country'])
                dt = cadastrar_cidade(cd)
                obj = checar_tempo(id=dt.id, cidade=dt, schema=cidade_schema)
                return obj
            else:
                obj = checar_tempo(id=check.id, cidade=check, schema=cidade_schema)
                return obj
        else:
            return make_response({'message': "Não foi possível checar cidade!"}, 404)
