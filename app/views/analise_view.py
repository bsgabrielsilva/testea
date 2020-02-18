from flask import request, jsonify, make_response

from app import app
from ..services import consultar_cidade, consultar_cidade_id, consultar_tempo
from ..db_services import listar_tempo_data, listar_tempo_max, listar_cidade_id
from ..entity import CidadeEntity, TempoEntity
from ..schemas import CidadeSchema
from ..utils import tratamento_tempo, checar_tempo, tratamento_media


@app.route('/analise', methods=['GET'])
def analise():
    di = request.args.get('data_inicial')
    df = request.args.get('data_final')
    dados = {'maiorTemperatura': {}, 'mediaPrecipitacao': []}
    if di is not None and df is not None:
        tp = listar_tempo_max(data_final=df, data_inicial=di)
        tc = listar_tempo_data(data_inicial=di, data_final=df)
        media = tratamento_media(tc)
        dados['maiorTemperatura'] = {'cidade': tp.cidade.nome,'temperatura': tp.max_temp, 'data': tp.data}
        dados['mediaPrecipitacao'] = media
        return make_response(jsonify(dados), 200)
    elif di is None and df is not None:
        return make_response({'message': 'Data inicial é parametro obrigatório!'})
    elif df is None and di is not None:
        return make_response({'message': 'Data final é parametro obrigatório!'})
    else:
        return make_response({'message': 'Data inicial e Data final são parametros obrigatórios!'})
