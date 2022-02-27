from flask import Flask, render_template

# Padrão para iniciar um site com FLask
app = Flask(__name__)

#cria 1ª página do site
#  toda página possui route(caminho que vem na URL apos o nome do domínio)
#  funções o que será exibido naquela página
#  decorator -> atribui nova funcionaidade para a função embaixo dela
@app.route("/")
def home_page():
    #render_template busca por padrão no diretorio templates. Basta informar nome da página
    return render_template('homepage.html')

@app.route("/contatos")
def contatos():
    return render_template('contatos.html')  

@app.route("/usuarios/<nome_usuario>")
def usuarios(nome_usuario):
    return render_template('usuarios.html', nome_usuario=nome_usuario)
    
#coloca o site no ar
if __name__ =="__main__":
    app.run(debug=True)

