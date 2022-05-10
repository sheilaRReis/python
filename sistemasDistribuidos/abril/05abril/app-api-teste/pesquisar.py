import json
import requests
def get_product_list():
    url = 'http://127.0.0.1:5000/api-loja/produtos'
    try:
        response = requests.get(url, headers={'content-type': 'application/json'})
        print(response.text)
        print("HTTP Status Code:" + str(response.status_code))
    except requests.exceptions.HTTPError as error:
        print(error)

def get_product(product_id=None):
    try:
        url = 'http://127.0.0.1:5000/api-loja/produtos/'+str(product_id)
        response = requests.get(url, headers={'content-type': 'application/json'})
        print(response.text)
        print("HTTP Status Code:" + str(response.status_code))
    except requests.exceptions.HTTPError as error:
        print(error)

if __name__ == '__main__':
    # get_product_list()
    get_product(34)