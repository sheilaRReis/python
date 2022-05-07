import json
import requests
dado = {'descricao':'outro produto qlqr','ganhopercentual': '1.5'}
dado_json = json.dumps(dado)
url = 'http://127.0.0.1:5000/api-loja/inserir'
r = requests.post(url, data=dado_json, headers={'content-type': 'application/json'})
print(r.text)