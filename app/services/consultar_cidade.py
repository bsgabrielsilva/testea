from app import app
import requests


def consultar_cidade(cidade, estado):
    TOKEN = "b22460a8b91ac5f1d48f5b7029891b53"
    url = f"http://apiadvisor.climatempo.com.br/api/v1/locale/city?name={cidade}&state={estado}&token={TOKEN}"
    r = requests.get(url)
    if r.status_code == 200:
        return r.json()[0]
    else:
        return "Alguma coisa deu errado na solicitação!"
