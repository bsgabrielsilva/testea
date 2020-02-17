from app import app
import requests


def consultar_tempo(cidade_id):
    TOKEN = "b22460a8b91ac5f1d48f5b7029891b53"
    url = f"http://apiadvisor.climatempo.com.br/api/v1/forecast/locale/{cidade_id}/days/15?token={TOKEN}"
    r = requests.get(url)
    if r.status_code == 200:
        return r.json()['data']
    else:
        return None
