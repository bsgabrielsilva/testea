from app import ma
from marshmallow import fields
from ..models import Tempo


class TempoSchema(ma.ModelSchema):
    class Meta:
        model = Tempo
        fields = ('id', 'data', 'probabilidade', 'precipitacao', 'max_temp', 'min_temp')

    id = fields.Integer(required=True)
    data = fields.Date(required=True)
    probabilidade = fields.Integer(required=True)
    precipitacao = fields.Integer(required=True)
    max_temp = fields.Integer(required=True)
    min_temp = fields.Integer(required=True)
