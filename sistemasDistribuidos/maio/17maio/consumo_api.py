import requests

endpoint1 = 'http://127.0.0.1:5000/auth'
endpoint2 = 'http://127.0.0.1:5000/protect'
credentials = {"user": "elsonabreu", "password": "12345"}
r = requests.post(url=endpoint1, json=credentials)
if r.status_code == 200:
    # Obtendo token
    token = r.json()
    signature = token['token']
    # Removendo sinalizacao de "bytes" da string (caractere 'b' e apostrofos)
    signature = signature.replace('b\'', '')
    signature = signature.replace('\'', '')
    # Enviando o token para endpoint protegido
    r = requests.post(url=endpoint2, json={'token': signature})
    if r.status_code == 200:
        print('Acesso concedido : ' + r.text )
    else:
        print('Acesso negado : ' + r.text)
else:
    print('Falha na requisicao.')