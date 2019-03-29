from app import app
from flask import session, redirect, url_for, request
from extra import *
from models import Order


@app.route('/manager-panel')
def manager_panel():
    if 'email' not in session:
        return redirect(url_for('index'))
    user = get_current_user()
    if user.role < 2:
        return redirect(url_for('index'))
    orders = Order.query.filter_by(shown=1).all()
    result = []
    for i in range(len(orders)):
        prods = eval(orders[i].products)
        result.append([orders[i], get_real_price(prods), get_predesc(prods)])
    return render('manager-panel.html', orders=result)


@app.route('/order-hide/<int:id>')
def order_hide(id):
    if 'email' not in session:
        return redirect(url_for('index'))
    if get_current_user().role < 2:
        return redirect(url_for('index'))
    order = Order.query.filter_by(id=id).first()
    order.shown = 1 - order.shown
    update_db(order)
    return redirect(url_for('manager_panel'))


@app.route('/delete-order/<int:id>')
def delete_order(id):
    if 'email' not in session:
        return redirect(url_for('index'))
    if get_current_user().role < 2:
        return redirect(url_for('index'))
    order = Order.query.filter_by(id=id).first()
    db.session.delete(order)
    db.session.commit()
    return redirect(url_for('manager_panel'))


@app.route('/edit-order-status/<int:id>', methods=['GET', 'POST'])
def edit_order_status(id):
    if 'email' not in session:
        return redirect(url_for('index'))
    if get_current_user().role < 2:
        return redirect(url_for('index'))
    if request.method == 'GET':
        return render('edit-order-status.html', id=id)
    else:
        order = Order.query.filter_by(id=id).first()
        order.status = int(request.form['status'][0])
        update_db(order)
        if order.status == 0:
            send_message(MESSAGE_SUCCESS, 'Ваш заказ №{} успешно оформлен. Вы можете отслеживать его в разделе "Мои заказы"'
                         .format(order.id), order.user)
        elif order.status == 1:
            send_message(MESSAGE_NOTIFICATION, 'Ваш заказ №{} сформирован и направляется к вам'
                         .format(order.id), order.user)
        elif order.status == 2:
            send_message(MESSAGE_SUCCESS, 'Ваш №{} заказ успешно доставлен'
                         .format(order.id), order.user)
        elif order.status == 3:
            send_message(MESSAGE_ERROR, 'Ваш заказ №{} отменен нашим менеджером. Свяжитесь с нами для выяснения подробностей'
                         .format(order.id), order.user)
        return redirect(url_for('manager_panel'))


@app.route('/send_msg/<int:user_id>', methods=['GET', 'POST'])
def send_msg(user_id):
    if 'email' not in session:
        return redirect(url_for('index'))
    if get_current_user().role < 2:
        return redirect(url_for('index'))
    if request.method == 'GET':
        return render('send-message.html', user_id=user_id)
    else:
        user = User.query.filter_by(id=user_id).first()
        send_message(int(request.form['type'][0]), request.form['msg'], user)
        return redirect(url_for('manager_panel'))


@app.route('/order-info/<int:id>')
def order_info(id):
    if 'email' not in session:
        return redirect(url_for('index'))
    order = Order.query.filter_by(id=id).first()
    current_user = get_current_user()
    if order.user.id != current_user.id and current_user.role < 2:
        return redirect(url_for('index'))
    products = eval(order.products)
    summa = 0
    for i in range(len(products)):
        prod = Product.query.filter_by(id=products[i]['id']).first()
        real_price = int(prod.price * (1 - prod.discount / 100))
        products[i] = [prod, real_price, products[i]['count'], i]
        summa += real_price * products[i][2] + products[i][0].delivery
    return render('order-info.html', order=order, products=products, sum=summa)


@app.route('/user-info/<int:user_id>')
def user_info(user_id):
    if 'email' not in session:
        return redirect(url_for('index'))
    if get_current_user().role < 2:
        return redirect(url_for('index'))
    user = User.query.filter_by(id=user_id).first()
    return render('user-info.html', user=user, count_orders=len(user.orders))
