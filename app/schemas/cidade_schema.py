from app import ma
from marshmallow import fields
from ..models import Cidade


class CidadeSchema(ma.ModelSchema):
    class Meta:
        model = Cidade
        fields = ('id', 'nome', 'estado', 'pais')

    id = fields.Integer(required=True)
    nome = fields.String(required=True)
    estado = fields.String(required=True)
    pais = fields.String(required=True)
