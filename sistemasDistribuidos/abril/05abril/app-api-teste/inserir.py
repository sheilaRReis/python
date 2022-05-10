import json
import requests
def create_product():
    new_product = {'descricao':'produto bb','ganhopercentual': '1.5'}
    new_product_json = json.dumps(new_product)
    url = 'http://127.0.0.1:5000/api-loja/produtos'
    try:
        response = requests.post(url, data=new_product_json, headers={'content-type': 'application/json'})
        print(response.text)
        print("HTTP Status Code:" + str(response.status_code))
    except requests.exceptions.HTTPError as error:
        print(error)

if __name__ == '__main__':
    create_product()
