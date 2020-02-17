from flask import make_response, jsonify
from ..db_services import cadastrar_tempo, listar_tempo_data_cidade
from ..services import consultar_tempo
from ..utils import tratamento_tempo
from ..entity import TempoEntity


def checar_tempo(id, cidade, schema):
    if id is not None:
        dados = consultar_tempo(cidade_id=id)
        if dados is not None:
            tratado = tratamento_tempo(dados)
            for t in tratado:
                teste = listar_tempo_data_cidade(data=t['data'], cidade=cidade)
                if teste is None:
                    cadastrar_tempo(TempoEntity(data=t['data'], probabilidade=t['probabilidade'],
                                                precipitacao=t['precipitacao'], max_temp=t['max_temp'],
                                                min_temp=t['min_temp'], cidade=cidade))
            return make_response(schema.jsonify(cidade), 200)
        else:
            return make_response({'message': 'Algo de errado na solicitação! A consulta não retornou dados!'}, 404)
    else:
        return make_response({'message': 'Parametro id é obrigatório!'}, 400)