import jwt
import datetime

print('-----------------------------------------')
# Obtendo a data/hora atual
datahora_emissao = datetime.datetime.now()
# Somando 30 segundos a data/hora atual
datahora_expirar = datahora_emissao + datetime.timedelta(seconds=10)
print('Data/hora de emissao:')
print(datahora_emissao)
print('Data/hora para expirar:')
print(datahora_expirar)
# Convertendo para o formato "timestamp", requerido pelo JWT
datahora_emissao = datahora_emissao.timestamp()
datahora_expirar = datahora_expirar.timestamp()
print('-----------------------------------------')
payload = {
    'id': '12345',
    'iat': datahora_emissao,
    'exp': datahora_expirar
}
print('Meu payload: ')
print(payload)
print('-----------------------------------------')
token_encode = jwt.encode(payload, "chavesecreta", algorithm="HS256")
print('Token codificado: ')
print(token_encode)
print('-----------------------------------------')
token_decode = jwt.decode(token_encode, "chavesecreta", algorithms=["HS256"])
print('Token decodificado: ')
print(token_decode)
print('-----------------------------------------')
token_datahora_emissao = datetime.datetime.fromtimestamp(token_decode['iat'])
token_datahora_expirar = datetime.datetime.fromtimestamp(token_decode['exp'])
print('Token decodificado - data/hora da emissao:')
print(token_datahora_emissao)
print('Token decodificado - data/hora de expirar:')
print(token_datahora_expirar)