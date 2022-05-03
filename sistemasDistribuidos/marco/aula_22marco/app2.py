
import requests

url = 'https://viacep.com.br/ws/'
logradouro = 'Rua dos Aimores'
cidade     = 'Belo Horizonte'
estado     = 'MG'
formato = '/json/'

r = requests.get(url + '/' +estado + '/' + cidade + '/' + logradouro  + formato)

if (r.status_code == 200):
    print('JSON : ', r.json())
else:
    print('Nao houve sucesso na requisicao.')
