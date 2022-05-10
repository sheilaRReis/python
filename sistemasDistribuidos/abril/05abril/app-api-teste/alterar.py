import json
import requests
def update_product_list():
    product_list = [{'descricao':'C1111oca Cola','ganhopercentual': '12.35', 'idproduto':15}, 
                    {'descricao':'Gu111araná','ganhopercentual': '17.25', 'idproduto':16}]
    product_json = json.dumps(product_list)
    url = 'http://127.0.0.1:5000/api-loja/produtos'
    try:
        response = requests.put(url, data=product_json, headers={'content-type': 'application/json'})
        print(response.text)
        print("HTTP Status Code:" + str(response.status_code))
    except requests.exceptions.HTTPError as error:
        print(error)

def update_product(product_id=None):
    product = {'descricao':'22','ganhopercentual': '1.7','idproduto':product_id}
    product_json = json.dumps(product)
    url = 'http://127.0.0.1:5000/api-loja/produtos/' + str(product_id)
    try:
        response = requests.put(url, data=product_json, headers={'content-type': 'application/json'})
        print(response.text)
        print("HTTP Status Code:" + str(response.status_code))
    except requests.exceptions.HTTPError as error:
        print(error)
    
if __name__ == '__main__':
    update_product(18)
    update_product_list()