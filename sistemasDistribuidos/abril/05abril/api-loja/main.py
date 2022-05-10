from math import prod
import sqlite3
from sqlite3 import Error
from flask import Flask, request, jsonify, abort
from datetime import date

app = Flask(__name__)

def connect_bd():
    return sqlite3.connect('C:\\Users\\Sheila\\dev\\cursoExtensao_Python\\python\\sistemasDistribuidos\\abril\\05abril\\api-loja\\database\\db-loja.db')
#############################################################################################################################
# 1) GET: pesquisar

# /produtos método GET -> pesquisar todos
@app.route('/api-loja/produtos', methods=['GET'])
def list_produtos():
    try:
        conn = connect_bd()
        sql = '''SELECT * FROM produtos'''
        cur = conn.cursor()
        cur.execute(sql)
        registros = cur.fetchall()
        if registros:
            nomes_colunas = [x[0] for x in cur.description]
            json_dados = []
            for reg in registros:
                json_dados.append(dict(zip(nomes_colunas, reg)))
            return jsonify(json_dados, 200)
        else:
            return jsonify({'mensagem': 'registro nao encontrado'}, 404)
    except Error as e:
        return jsonify({'mensagem': e}, 400)
    finally:
        conn.close()

# /produtos/id método GET -> pesquisar por id
@app.route('/api-loja/produtos/<int:idproduto>', methods=['GET'])
def pesquisar(idproduto=None):
    if idproduto == None:
        return jsonify({'mensagem': 'parametro invalido'})
    else:
        try:
            conn = connect_bd()
            if idproduto == 0:
                sql = '''SELECT * FROM produtos'''
            else:
                sql = '''SELECT * FROM produtos WHERE idproduto = ''' + str(idproduto)
            cur = conn.cursor()
            cur.execute(sql)
            registros = cur.fetchall()
            if registros:
                nomes_colunas = [x[0] for x in cur.description]
                json_dados = []
                for reg in registros:
                    json_dados.append(dict(zip(nomes_colunas, reg)))
                return jsonify(json_dados, 200)
            else:
                return jsonify({'mensagem': 'registro nao encontrado'},404)
        except Error as e:
            return jsonify({'mensagem': e}, 400)
        finally:
            conn.close()

#############################################################################################################################
# 2) POST: inserir

#   /produtos método POST -> criar produto
@app.route('/api-loja/produtos', methods=['POST'])
def create_product():
    if request.method == 'POST':
        dados = request.get_json()
        descricao = dados['descricao']
        ganhopercentual = dados['ganhopercentual']
        datacriacao = date.today()
        if descricao and ganhopercentual and datacriacao:
            registro = (descricao, ganhopercentual, datacriacao)
            try:
                conn = connect_bd()
                sql = ''' INSERT INTO produtos(descricao, ganhopercentual, datacriacao) VALUES(?,?,?)   '''
                cur = conn.cursor()
                cur.execute(sql, registro)
                conn.commit()
                # Se um método POST cria um novo recurso, ele retornará o código de status HTTP 201 (Criado).
                return jsonify({'mensagem': 'registro inserido com sucesso'}, 201)
            except Error as e:
                return jsonify({'mensagem': e}, 400)
            finally:
                conn.close()
        else:
            # Se o cliente coloca os dados inválidos na solicitação, o servidor deve retornar o código de status HTTP 400 (Solicitação incorreta).
            return jsonify({'mensagem': 'campos <descricao> e <ganhopercentual> sao obrigatorios'}, 400)

#############################################################################################################################
# 3) DELETE: excluir

# Deletar todos produtos
@app.route('/api-loja/produtos', methods=['DELETE'])
def delete_all_products():
    try:        
        conn = connect_bd()
        sql = '''DELETE FROM produtos  '''
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        # Se a operação de exclusão for bem-sucedida, o servidor Web deverá responder com um código de status HTTP 204
        return jsonify({'mensagem': 'Registros excluídos'}, 204)
    except Error as e:
        return jsonify({'mensagem': e}, 404)
    finally:
        conn.close()

#Deletar produto por id
@app.route('/api-loja/produtos/<int:idproduto>', methods=['DELETE'])
def delete_product(idproduto=None):
    if idproduto == None:
        return jsonify({'mensagem': 'parametro invalido'}, 400)
    else:
        try:                
            conn = connect_bd()
            sql = '''DELETE FROM produtos WHERE idproduto = ? ''' + str(idproduto)
            cur = conn.cursor()
            cur.execute(sql)
            conn.commit()
            # Se a operação de exclusão for bem-sucedida, o servidor Web deverá responder com um código de status HTTP 204
            return jsonify({'mensagem': 'registro excluido'}, 204)
        except Error as e:
            return jsonify({'mensagem': e}, 404)
        
        finally:
            conn.close()


#######################################################
# 4) PUT: alterar
#######################################################
# /produtos PUT -> Atualização em massa de produtos
@app.route('/api-loja/produtos', methods=['PUT'])
def edit_product_list():
    if request.method == 'PUT':
        dados = request.get_json()
        if dados:
            products = list()
            for i in range( len(dados) ):
                columnValues = (dados[i]['descricao'], dados[i]['ganhopercentual'], dados[i]['idproduto'])
                products.append(columnValues)
            try:
                conn = connect_bd()
                sql = ''' UPDATE produtos SET descricao=?, ganhopercentual=? WHERE idproduto = ?'''
                cur = conn.cursor()
                cur.executemany(sql, products)
                conn.commit()
                # Se o método PUT atualiza um recurso existente, ele retorna 200 (OK)
                return jsonify({'mensagem': 'Produtos alterados com sucesso'}, 200)
            except Error as e:
                # Em alguns casos, pode não ser possível atualizar um recurso existente. Nesse caso, considere 
                # que pode ser retornado o código de status HTTP 409 (Conflito).
                return jsonify({'mensagem': e}, 409)
            finally:
                conn.close()
        
    
# /produtos/id método PUT -> alterar
@app.route('/api-loja/produtos/<int:idproduto>', methods=['PUT'])
def edit_product(idproduto=None):
    if request.method == 'PUT':
        if idproduto == None:
            return jsonify({'mensagem': 'parametro invalido'})
        else:
            dados = request.get_json()
            descricao = dados['descricao']
            ganhopercentual = dados['ganhopercentual']

            if descricao and ganhopercentual and idproduto:
                registro = (descricao, ganhopercentual, idproduto)
                try:
                    conn = connect_bd()
                    sql = ''' UPDATE produtos SET descricao=?, ganhopercentual=? WHERE idproduto = ?'''
                    cur = conn.cursor()
                    cur.execute(sql, registro)
                    conn.commit()
                    # Se o método PUT atualiza um recurso existente, ele retorna 200 (OK)
                    return jsonify({'mensagem': 'registro alterado com sucesso'}, 200)
                except Error as e:
                    # Em alguns casos, pode não ser possível atualizar um recurso existente. 
                    # Nesse caso, considere que pode ser retornado o código de status HTTP 409 (Conflito).
                    return jsonify({'mensagem': e}, 409)
                finally:
                    conn.close()
            else:
                return jsonify({'mensagem': 'campos < descricao > , < ganhopercentual > e < idproduto > sao obrigatorios'}, 409)

#######################################################
# 5) UrlPoint nao localizado
#######################################################
@app.errorhandler(404)
def endpoint_nao_encontrado(e):
    return jsonify({'mensagem': 'erro - endpoint nao encontrado'}), 404

@app.errorhandler(405)
def endpoint_nao_encontrado(e):
    return jsonify({'mensagem': 'erro - endpoint nao encontrado'}), 405
#######################################################
# XX Execucao da Aplicacao
#######################################################
if __name__ == '__main__':
    app.run()
