import requests
import codecs
url = 'http://www.google.com/search' + '?q' + 'elson de abreu'
r = requests.get(url)

if (r.status_code == 200):
    print('Retorno : ', r.text)
    file_name = 'output.txt'
    with codecs.open(file_name, 'w', encoding='utf8') as f:
        f.write(r.text)
  
    f.close()
else:
    print('Nao houve sucesso na requisicao.')
