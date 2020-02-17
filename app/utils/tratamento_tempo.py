def tratamento_tempo(dados):
    tratamento = []
    for i in dados:
        tratamento.append({'data': i['date'], 'probabilidade': i['rain']['probability'],
                           'precipitacao': i['rain']['precipitation'], 'max_temp': i['temperature']['max'],
                           'min_temp': i['temperature']['min']})
    return tratamento
