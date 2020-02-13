from flask_restful import Resource


class CidadeList(Resource):
    def get(self):
        return "Olá mundo"
