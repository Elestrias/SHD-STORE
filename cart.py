from app import app
from extra import *
from flask import redirect, url_for
from models import Product


@app.route('/basket')
def basket():
    if 'basket' not in session:
        session['basket'] = []
    products = session['basket']
    summa = 0
    for i in range(len(products)):
        prod = Product.query.filter_by(id=products[i]['id']).first()
        real_price = int(prod.price * (1 - prod.discount / 100))
        products[i] = [prod, real_price, products[i]['count'], i]
        summa += real_price * products[i][2]
    return render('basket.html', products=products, sum=summa)


@app.route('/add_cart/<int:id>')
def add_cart(id):
    session['basket'] = session['basket'] + [{'id': id, 'count': 1}]
    print(session['basket'])
    return redirect(url_for('basket'))


@app.route('/remove_cart/<int:id>')
def remove_cart(id):
    b = session['basket']
    new = []
    for i in range(len(b)):
        if i != id:
            new.append(b[i])
    session['basket'] = new
    return redirect(url_for('basket'))
