from email import message
from math import prod
from flask import Flask
from flask_restful import Resource, Api, abort, fields, marshal_with, reqparse
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = ('sqlite:///db-loja.db')
db = SQLAlchemy(app)

class ProdutoModel(db.Model):
    __tablename__ = 'produtos'
    idproduto = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String)
    ganhopercentual = db.Column(db.Float)

product_post_args = reqparse.RequestParser()
product_post_args.add_argument("descricao", type=str, help="O campo descrição deve ser informado", required=True)
product_post_args.add_argument("ganhopercentual", type=float, help="O campo ganho percentual deve ser informado", required=True)

product_update_args = reqparse.RequestParser()
product_update_args.add_argument("descricao", type=str)
product_update_args.add_argument("ganhopercentual", type=float)

resource_fields = {
    'idproduto' : fields.Integer,
    'descricao' : fields.String,
    'ganhopercentual' : fields.Float
}


class ProdutosList(Resource):
    def get(self):
        produtos = ProdutoModel.query.all()
        produtosList = {}
        for produto in produtos:
            produtosList[produto.idproduto] = {"descricao" : produto.descricao, "ganhopercentual": produto.ganhopercentual}
        return produtosList

class Produtos(Resource):
    @marshal_with(resource_fields)
    def get(self, product_id):
        produto = ProdutoModel.query.filter_by(idproduto=product_id).first()
        if not produto:
            abort(404, message='Não foi possível encontrar o produto')
        return produto

    @marshal_with(resource_fields)
    def post(self):
        args = product_post_args.parse_args()
        produto = ProdutoModel(descricao=args['descricao'], ganhopercentual=args['ganhopercentual'])
        db.session.add(produto)
        db.session.commit()
        return produto,201

    @marshal_with(resource_fields)
    def put(self, product_id):
        args = product_update_args.parse_args()
        produto = ProdutoModel.query.filter_by(idproduto=product_id).first()
        if not produto:
            abort(404, message='Produto não encontrado')
        if args['descricao']:
            produto.descricao =  args['descricao']
        if args['ganhopercentual']:
            produto.ganhopercentual =  args['ganhopercentual']
        db.session.commit()
        return produto

    def delete(self, product_id):
        produto = ProdutoModel.query.filter_by(idproduto=product_id).first()
        db.session.delete(produto)
        return 'Produto excluído com sucesso! ', 204
        
api.add_resource(Produtos, '/api-loja/produtos/<int:product_id>')
api.add_resource(ProdutosList, '/api-loja/produtos')

if __name__ == '__main__':
    app.run(debug=True) 