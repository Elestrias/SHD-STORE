from app import app
from extra import *
from flask import redirect, url_for, request


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


@app.route('/lk-pass', methods=['GET', 'POST'])
def lk_pass():
    if 'email' not in session:
        return redirect(url_for('index'))
    if request.method == 'GET':
        return render('lk-pass.html')
    elif request.method == 'POST':
        if request.form['old-pass'] == '' or request.form['new-pass'] == '' or request.form['new-rpass'] == '':
            return render('lk-pass.html', empty=True)
        if request.form['new-pass'] != request.form['new-rpass']:
            return render('lk-pass.html', diff=True)
        user = get_current_user()
        if hash_password(request.form['old-pass']) != user.password:
            return render('lk-pass.html', bad_old=True)
        user.password = hash_password(request.form['new-pass'])
        update_db(user)
        return render('lk-pass.html', success=True)
