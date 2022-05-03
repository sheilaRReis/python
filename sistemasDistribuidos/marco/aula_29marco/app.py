import requests
import sqlite3
from sqlite3 import Error
from datetime import date

#Recupera cotações do dólar e euro da API HGBrasil, e retorna o registro
def get_api_values():
    url = 'https://api.hgbrasil.com/finance?format=json-cors&key=7eebc86b'

    resposta = requests.get(url)

    if resposta.status_code == 200:
        json = resposta.json()
        current_date = str(date.today().strftime('''%d-%m-%Y'''))
        dolar_value = json['results']['currencies']['USD']['buy']
        euro_value  = json['results']['currencies']['EUR']['buy']
        registro = (current_date, dolar_value, euro_value)
        return registro
    else:
        print('Falha na consulta à API')

# Cria tabela moedas, caso a mesma ainda não exista
def create_table_moedas():
    try:
        conn = sqlite3.connect('bdcotacoes.db')
        cursor = conn.cursor()

        # SQL que verifica se a tabela Moedas já existe
        sql = '''SELECT count(name) FROM sqlite_master WHERE type='table' AND name='moedas' '''
        cursor.execute(sql)

        if cursor.fetchone()[0]==1 : 
            print('Tabela Moedas já existe.')
        else:

            sql = """create table moedas(
                        data text,
                        dolar real,
                        euro real
                            ) """
            cursor.execute(sql)

            return 'Tabela Moedas criada com sucesso.'
    except Error as e:
        return ('Erro: ', e)
    finally:
        conn.close()

#Insere registro na tabela moedas
def insert_moedas(registro):
    try:
        conn = sqlite3.connect('bdcotacoes.db')
        sql = ''' INSERT INTO moedas(data, dolar, euro) VALUES(?,?,?) '''

        cursor = conn.cursor()
        cursor.execute(sql, registro)
        conn.commit()

        print('Registro inserido com sucesso')

    except Error as e:
       print('Erro: ', e)
    finally:
       conn.close()


if __name__ == '__main__':
    registro = get_api_values()
    create_table_moedas()
    insert_moedas(registro=registro)
