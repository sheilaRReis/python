# Tutorial Flask CRUD Application Full Course With SQLAlchemy | Python Flask
# Disponível em: https://www.youtube.com/watch?v=XTpLbBJTOM4
# TimeStamp = 24:44
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)