import json
import requests
dado = {'descricao':'Fanta','ganhopercentual': '1.7','idproduto': 1}
dado_json = json.dumps(dado)
url = 'http://127.0.0.1:5000/api-loja/alterar'
r = requests.put(url, data=dado_json, headers={'content-type': 'application/json'})
print(r.text)