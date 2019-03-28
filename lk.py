from app import app
from extra import *
from flask import redirect, url_for


@app.route('/lk-orders')
def lk_orders():
    if 'email' not in session:
        return redirect(url_for('index'))
    orders = get_current_user().orders
    result = []
    for i in range(len(orders)):
        prods = eval(orders[i].products)
        result.append([orders[i], get_real_price(prods), get_predesc(prods)])
    return render('lk-orders.html', orders=result)


@app.route('/lk-msg')
def lk_msg():
    if 'email' not in session:
        return redirect(url_for('index'))
    user = get_current_user()
    user.unread = 0
    update_db(user)
    return render('lk-msg.html', messages=sorted(user.messages, key=lambda x: x.date, reverse=True))


@app.route('/lk-pass')
def lk_pass():
    if 'email' not in session:
        return redirect(url_for('index'))
    return render('lk-pass.html')


@app.route('/manager-panel')
def manager_panel():
    if 'email' not in session:
        return redirect(url_for('index'))
    return render('manager-panel.html')
