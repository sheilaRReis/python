import requests
url = 'http://127.0.0.1:5000/api-loja/excluir/1'
r = requests.delete(url)
print(r.text)