from market import app

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#Sinc changes, without reestartig the server. Can't be used on production enviroment
app.debug = True
#URI - Uniform Resource Identifier != URL
app.config['SQLAlchemy_DATABASE_URI'] = 'sqlite:///market.db'
db = SQLAlchemy(app)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# app.config['SQLALCHEMY_DATABASE_URI']        = 'mysql://root:root@localhost/flaskmarketDB'

db.init_app(app)
db.create_all()

from market import routes
