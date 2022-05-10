from flask import Flask
import sqlite3
from sqlite3 import Error
from flask import Flask, jsonify, make_response
from flask_restful import Resource, Api, reqparse, fields
from sqlalchemy import true

app = Flask(__name__)
api = Api(app)

product_fields = {
    'id': fields.Integer,
    'descricao': fields.String,
    'ganhopercentual': fields.Float,
    'uri': fields.Url('task')
}

product_post_args = reqparse.RequestParser()
product_post_args.add_argument('descricao', type=str, help="O campo descrição deve ser informado", required=True)
product_post_args.add_argument('ganhopercentual', type=str, help="O campo ganho percentual deve ser informado", required=True)

product_update_args = reqparse.RequestParser()
product_update_args.add_argument('descricao', type=str)
product_update_args.add_argument('ganhopercentual', type=float)
def connect_to_db():
    conn = sqlite3.connect('C:\\Users\\Sheila\\dev\\cursoExtensao_Python\\python\\sistemasDistribuidos\\abril\\05abril\\api-loja\\database\\db-loja.db')
    return conn

class ProdutoListAPI(Resource):
    def get(self):
        try:
            conn = connect_to_db()
            sql = '''SELECT * FROM produtos'''
            cur = conn.cursor()
            cur.execute(sql)
            registros = cur.fetchall()
            if registros:
                nomes_colunas = [x[0] for x in cur.description]
                json_dados = []
                for reg in registros:
                    json_dados.append(dict(zip(nomes_colunas, reg)))
                return jsonify(json_dados)
            else:
                return jsonify({'mensagem': 'registro nao encontrado'}, 404)
        except Error as e:
            return jsonify({'mensagem': e})
        finally:
            conn.close()

class ProdutoAPI(Resource):
    def get(self, product_id):
        if product_id == None:
            return jsonify({'mensagem': 'parametro invalido'})
        else:
            try:
                conn = connect_to_db()
                if product_id == 0:
                    sql = '''SELECT * FROM produtos'''
                else:
                    sql = '''SELECT * FROM produtos WHERE idproduto = ''' + str(product_id)
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
                    return jsonify({'mensagem': 'registro não encontrado'}, 404)
            except Error as e:
                return jsonify({'mensagem': e})
            finally:
                conn.close()
    def post(self):
        args = product_post_args.parse_args()
        

api.add_resource(ProdutoListAPI, '/api-loja/produtos', endpoint='produtos')
api.add_resource(ProdutoAPI, '/api-loja/produtos/<int:product_id>', endpoint='produto')

if __name__ == '__main__':
    app.run(debug=True) 