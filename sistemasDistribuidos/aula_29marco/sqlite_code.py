# Para utilizar e preciso instalar a lib do SQLite3
# pip3 install pysqlite3

import sqlite3
from sqlite3 import Error
from datetime import date

def criar_bancodados():
    try:
        conn = sqlite3.connect('bdcotacoes.db')
        
        sql = """create table moedas(
                    data text,
                    dolar real,
                    euro real
                        ) """

        cursor = conn.cursor()
        cursor.execute(sql)

        return 'Tabela Moedas criada com sucesso.'

    except Error as e:
        return ('Erro: ', e)
    finally:
        conn.close()




if __name__ == '__main__':
    criar_bancodados()

    current_date = str(date.today())
    registro = (current_date, 1, 10)

    try:
        conn = sqlite3.connect('bdcotacoes.db')

        sql = ''' INSERT INTO moedas(data, dolar, euro) VALUES(?,?,?) '''

        cursor = conn.cursor()
        cursor.execute(sql, registro)
        conn.commit()

        print('registro inserido com sucesso')

    except Error as e:
       print('Erro: ', e)
    finally:
       conn.close()