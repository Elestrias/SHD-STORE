from flask import request, url_for
from werkzeug.utils import redirect

from app import app
from extra import *


@app.route('/category/<categ>')
def category(categ):
    cat = Category.query.filter_by(engname=categ).first()
    products = cat.products[:]
    for i in range(len(products)):
        products[i] = [products[i], int(products[i].price * (1 - products[i].discount / 100))]
    return render('category.html', category=cat, products=products, len=len(products))


@app.route('/product/<int:id>')
def product(id):
    prod = Product.query.filter_by(id=id).first()
    real_price = int(prod.price * (1 - prod.discount / 100))
    return render('product.html', product=prod, real_price=real_price)


@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        products = Product.query.filter(Product.name.like('%' + request.form['s'] + '%')).all()
        for i in range(len(products)):
            products[i] = [products[i], int(products[i].price * (1 - products[i].discount / 100))]
        return render('search.html', search_query=request.form['s'], products=products, len=len(products))
    else:
        return redirect(url_for('index'))
