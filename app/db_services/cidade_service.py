from ..models import Cidade
from app import db


def cadastrar_cidade(cidade):
    cidade_bd = Cidade(id=cidade.id, nome=cidade.nome, estado=cidade.estado, pais=cidade.pais)
    db.session.add(cidade_bd)
    db.session.commit()
    return cidade_bd


def listar_cidade_id(id):
    cidade = Cidade.query.filter_by(id=id).first()
    return cidade


def remover_cidade(cidade):
    db.session.delete(cidade)
    db.session.commit()

