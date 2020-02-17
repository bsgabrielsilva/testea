from app import db
from .cidade_model import Cidade


class Tempo(db.Model):
    __tablename__ = "tempo"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    data = db.Column(db.Date(), nullable=False)
    probabilidade = db.Column(db.Integer(), nullable=False)
    precipitacao = db.Column(db.Integer(), nullable=False)
    max_temp = db.Column(db.Integer(), nullable=False)
    min_temp = db.Column(db.Integer(), nullable=False)

    cidade_id = db.Column(db.Integer, db.ForeignKey("cidade.id"))
    cidade = db.relationship(Cidade, backref=db.backref("tempo", lazy="dynamic"))
