import requests
def delete_product(product_id=None):
    try:
        url = 'http://127.0.0.1:5000/api-loja/produtos/'+str(product_id)
        response = requests.delete(url)
        print(response.text)
        print("HTTP Status Code:" + str(response.status_code))
    except requests.exceptions.HTTPError as error:
        print(error)

def delete_all_products():
    try:
        url = 'http://127.0.0.1:5000/api-loja/produtos'
        response = requests.delete(url)
        print(response.text)
        print("HTTP Status Code:" + str(response.status_code))
    except requests.exceptions.HTTPError as error:
        print(error)


if __name__ == '__main__':
    delete_product(99)
    # delete_all_products()