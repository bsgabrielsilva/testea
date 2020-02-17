from app import ma
from marshmallow import fields
from ..models import Cidade
from .tempo_schema import TempoSchema


class CidadeSchema(ma.ModelSchema):
    class Meta:
        model = Cidade
        fields = ('id', 'nome', 'estado', 'pais', 'tempo')

    id = fields.Integer(required=True)
    nome = fields.String(required=True)
    estado = fields.String(required=True)
    pais = fields.String(required=True)
    tempo = fields.List(fields.Nested(TempoSchema))
