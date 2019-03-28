from app import app
from extra import *


@app.route('/lk-orders')
def lk_orders():
    return render('lk-orders.html')


@app.route('/lk-msg')
def lk_msg():
    user = get_current_user()
    user.unread = 0
    update_db(user)
    return render('lk-msg.html', messages=sorted(user.messages, key=lambda x: x.date, reverse=True))


@app.route('/lk-pass')
def lk_pass():
    return render('lk-pass.html')


@app.route('/manager-panel')
def manager_panel():
    return render('manager-panel.html')
