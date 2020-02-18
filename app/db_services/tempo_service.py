from ..models import Tempo, Cidade
from app import db
from datetime import datetime


def cadastrar_tempo(tempo):
    new_data = datetime.strptime(tempo.data, '%Y-%m-%d')
    tempo_bd = Tempo(data=new_data, probabilidade=tempo.probabilidade, precipitacao=tempo.precipitacao,
                     max_temp=tempo.max_temp, min_temp=tempo.min_temp, cidade=tempo.cidade)
    db.session.add(tempo_bd)
    db.session.commit()
    return tempo_bd


def listar_tempo_id(id):
    tempo = Tempo.query.filter_by(id=id).first()
    return tempo


def listar_tempo_data_cidade(data, cidade):
    tempo = Tempo.query.with_parent(cidade).filter_by(data=data).first()
    return tempo


def listar_tempo_data(data_inicial, data_final):
    tempo = Tempo.query.filter((Tempo.data >= data_inicial) & (Tempo.data <= data_final)).all()
    return tempo


def listar_tempo_max(data_inicial, data_final):
    tempo = Tempo.query.filter((Tempo.data >= data_inicial) & (Tempo.data <= data_final)).\
        order_by(Tempo.max_temp.desc()).first()
    return tempo


def listar_tempo_cidade(cidade):
    tempo = Tempo.query.with_parent(cidade).all()
    return tempo


def remover_tempo(tempo):
    db.session.delete(tempo)
    db.session.commit()

