from market import app
from flask import render_template
from market.models import Item
#Decorator 
@app.route('/')
@app.route('/home')
def home_page():
    #render_template redirects to html file created in the templates folder
    return render_template('/home.html')

@app.route('/market')
def market_page():
    items = Item.query.all()
    return render_template('/market.html', items=items)

#Dinamic route 
# @app.route('/about/<username>')
# def about_page(username):
#     return f'<h1>About page of {username}</h1>'
