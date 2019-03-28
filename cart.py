from app import app
from extra import *
from flask import redirect, url_for, request
from models import Product, Order


@app.route('/basket')
def basket():
    if 'email' not in session:
        return redirect(url_for('index'))
    if 'basket' not in session:
        session['basket'] = []
    products = session['basket']
    summa = 0
    for i in range(len(products)):
        prod = Product.query.filter_by(id=products[i]['id']).first()
        real_price = int(prod.price * (1 - prod.discount / 100))
        products[i] = [prod, real_price, products[i]['count'], i]
        summa += real_price * products[i][2] + products[i][0].delivery
    return render('basket.html', products=products, sum=summa)


@app.route('/add_cart/<int:id>')
def add_cart(id):
    if 'email' not in session:
        return redirect(url_for('index'))
    session['basket'] = session['basket'] + [{'id': id, 'count': 1}]
    return redirect(url_for('basket'))


@app.route('/remove_cart/<int:id>')
def remove_cart(id):
    if 'email' not in session:
        return redirect(url_for('index'))
    b = session['basket']
    new = []
    for i in range(len(b)):
        if i != id:
            new.append(b[i])
    session['basket'] = new
    return redirect(url_for('basket'))


@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    if request.method == 'GET':
        if 'email' not in session:
            return redirect(url_for('index'))
        if 'basket' not in session:
            session['basket'] = []
        if session['basket'] == []:
            return redirect(url_for('basket'))
        products = session['basket']
        summa = 0
        for i in range(len(products)):
            prod = Product.query.filter_by(id=products[i]['id']).first()
            real_price = int(prod.price * (1 - prod.discount / 100))
            products[i] = [prod, real_price, products[i]['count'], i]
            summa += real_price * products[i][2] + products[i][0].delivery
        return render('checkout.html', products=products, sum=summa)
    elif request.method == 'POST':
        user = get_current_user()
        order = Order(products=repr(session['basket']), delivery_point=int(request.form.get('point')[0]),
                      wishes=request.form['wishes'], user=user)
        update_db(order)
        send_message(MESSAGE_SUCCESS, 'Ваш заказ успешно оформлен. Вы можете отслеживать его в разделе "Мои заказы"', user)
        session['basket'] = []
        return redirect(url_for('proceed_checkout'))


@app.route('/proceed-checkout')
def proceed_checkout():
    return render('proceed-checkout.html')
