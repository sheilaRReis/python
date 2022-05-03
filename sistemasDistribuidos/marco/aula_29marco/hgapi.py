import requests

url = 'https://api.hgbrasil.com/finance?format=json-cors&key=7eebc86b'

resposta = requests.get(url)

if resposta.status_code == 200:
    json = resposta.json()
    print(json['results']['currencies'])
    print('Dolar: ')
    print(json['results']['currencies']['USD']['buy'])
    print('Euro: ')
    print(json['results']['currencies']['EUR']['buy'])
else:
    print('Falhou')