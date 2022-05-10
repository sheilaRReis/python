from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'data': 'Hello World!'}

class HelloName(Resource):
    def get(self, name):
        return {'data' : 'Hello, {}'.format(name)}

# Para cada recurso adicionado, deve ser criada uma classe com mesmo nome
# endpoint: http://127.0.0.1:5000/helloworld
api.add_resource(HelloWorld, '/helloworld')

# http://127.0.0.1:5000/helloworld/nome
api.add_resource(HelloName, '/helloworld/<string:name>')

if __name__ == '__main__':
    app.run(debug=True) 