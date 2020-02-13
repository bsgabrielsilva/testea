from app import db


class Cidade(db.Model):
    __tablename__ = "cidade"

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    nome = db.Column(db.String(100), nullable=False)
    estado = db.Column(db.String(2), nullable=False)
    pais = db.Column(db.String(2), nullable=False)