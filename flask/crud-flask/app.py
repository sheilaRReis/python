# Tutorial CRUD COMPLETO FLASK com SQLALCHEMY em Python - API REST e BANCO DE DADOS 2021
# Disponível em: https://www.youtube.com/watch?v=WDpPGFkI9UU&t=651s
#   Flask -> cria rotas da API
#   Response -> usada para criar o retorno da API
#   Request -> usada para trabalhar com o body(comum no método POST)
from flask import Flask, Response, request
from flask_sqlalchemy import SQLAlchemy 
import mysql.connector
import json

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI']        = 'mysql://root:root@localhost/crud_flaskDB'

db = SQLAlchemy(app)

class Usuario(db.Model):
    id    = db.Column(db.Integer, primary_key = True)
    nome  = db.Column(db.String(50))
    email = db.Column(db.String(100))
    
    def to_json(self):
        return {
            "id": self.id,
            "nome:": self.nome , 
            "email": self.email
         }
    
    # Para gerar tabelas, devemos abrir o Terminal, e digitar os seguintes comandos:
    # python<ENTER>     
    # from app import db <ENTER>
    # db.create_all()<ENTER> 

#Selecionar tudo
@app.route('/usuarios', methods=["GET"])
def seleciona_usuarios():
    user_objects = Usuario.query.all()
    user_json    = [user.to_json() for user in user_objects]
    print(user_json)
    return gera_response(200, "usuarios", user_json, "ok")

def gera_response(status, content_name, content, message=False ) :
    body = {}
    body[content_name] = content
    
    if(message) :
        body["message"] = message
    
    return Response(json.dumps(body), status=status, mimetype="application/json")

#Selecionar um usuário pelo Id
@app.route("/usuario/<id>")
def seleciona_usuario(id):
    user_object = Usuario.query.filter_by(id=id).first()
    user_json   = user_object.to_json()

    return gera_response(200, "usuario", user_json)

#Cadastrar usuário
@app.route("/usuario", methods=["POST"])
def cria_usuario():
    body = request.get_json()
    #Validar parametros
    try:
        usuario = Usuario(nome=body["nome"], email=body["email"])
        db.session.add(usuario)
        db.session.commit()
        return gera_response(201, "usuario", usuario.to_json(), "Usuario criado com sucesso!")
    except Exception as e:
        print("Erro: ",e)
        return gera_response(400, "usuario", {}, "Erro no cadastro de usuário")

# Update usuario - timestamp = 23:52
@app.route("/usuario/<id>", methods=["PUT"])
def atualiza_usuario(id):
    user_object = Usuario.query.filter_by(id=id).first()
    body = request.get_json()

    try:
        if("nome" in body):
            user_object.nome = body["nome"]
        if("email" in body):
            user_object.email = body["email"]
        db.session.add(user_object)
        db.session.commit()
        return gera_response(200, "usuario", user_object.to_json(), "Usuario atualizado com sucesso!")
    except Exception as e:
        print("Erro: ",e)
        return gera_response(400, "usuario", {}, "Erro ao atualizar usuário")
         
#Deletar usuário
@app.route("/usuario/<id>", methods=["DELETE"])
def deleta_usuario(id):    
    user_object = Usuario.query.filter_by(id=id).first()

    try:
        db.session.delete(user_object)
        db.session.commit()
        return gera_response(200, "usuario", user_object.to_json(), "Usuario excluido com sucesso!")
    except Exception as e:
        print("Erro: ",e)
        return gera_response(400, "usuario", {}, "Erro ao deletar usuário")

app.run()