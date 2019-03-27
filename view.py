from app import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/basket')
def basket():
    return render_template('basket.html')


@app.route('/lk-orders')
def lk_orders():
    return render_template('lk-orders.html')


@app.route('/lk-msg')
def lk_msg():
    return render_template('lk-msg.html')


@app.route('/lk-pass')
def lk_pass():
    return render_template('lk-pass.html')


@app.route('/manager-panel')
def manager_panel():
    return render_template('manager-panel.html')
