from app import app
import requests

TOKEN = app.config.get('TOKEN')


def consultar_cidade(cidade, estado):
    url = f"http://apiadvisor.climatempo.com.br/api/v1/locale/city?name={cidade}&state={estado}&token={TOKEN}"
    r = requests.get(url)
    if r.status_code == 200:
        return r.json()
    else:
        return "Alguma coisa deu errado na solicitação!"
