def tratamento_media(tempo):
    lista = []
    media = 0.0
    contador = 0
    lista_tratada = []
    for t in tempo:
        print(t.data)
        if not t.cidade in lista:
            lista.append(t.cidade)

    for i in lista:
        for td in tempo:
            if i == td.cidade:
                media = media + td.precipitacao
                contador += 1
        lista_tratada.append({'cidade': i.nome, 'estado': i.estado, 'pais': i.pais,
                              'media_precipitacao': float(format(float(media / contador), '.2f'))})
        media = 0.0
        contador = 0
    return lista_tratada