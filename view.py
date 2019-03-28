from flask_mail import Message
from app import app, mail
from flask import render_template, session, request, redirect, url_for
from models import db, User, Category, Product
import hashlib
from config import *


def render(temp, **kwargs):
    return render_template(temp, categories=Category.query.filter_by(shown=1).all(), **kwargs)


@app.route('/')
@app.route('/index')
def index():
    return render('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render('register.html')
    elif request.method == 'POST':
        if request.form['email'] == '':
            return render('register.html', email_empty=True)
        if len(request.form['password']) < 6:
            return render('register.html', pass_empty=True)
        if request.form['password'] != request.form['rpassword']:
            return render('register.html', diff_pass=True)
        if not request.form.get('accept'):
            return render('register.html', no_accept=True)
        if User.query.filter_by(email=request.form['email']).first() is not None:
            return render('register.html', user_exists=True)
        password = hashlib.md5((SALT + request.form['password']).encode('utf-8')).hexdigest()
        hashcode = hashlib.md5((request.form['email'] + request.form['password']).encode('utf-8')).hexdigest()
        user = User(email=request.form['email'], password=password, hashcode=hashcode)
        db.session.add(user)
        db.session.commit()
        msg = Message('Подтверждение учетной записи',
                      sender=("Робот интернет-магазина", "admin@shop.ru"),
                      recipients=[request.form['email']])
        msg.body = 'Вы можете подтвердить свою учетную запись, перейдя по {}'.format(ADDRESS + 'confirm/' + hashcode)
        mail.send(msg)
        return render('register.html', success=True)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render('login.html')
    elif request.method == 'POST':
        if request.form['email'] == '':
            return render('login.html', email_empty=True)
        if request.form['password'] == '':
            return render('login.html', pass_empty=True)
        user = User.query.filter_by(email=request.form['email']).first()
        if user is None:
            return render('login.html', bad_data=True)
        if user.password != hashlib.md5((SALT + request.form['password']).encode('utf-8')).hexdigest():
            return render('login.html', bad_data=True)
        if user.role == 0:
            return render('login.html', banned=True)
        if user.hashcode != '':
            return render('login.html', unactivated=True)
        session['email'] = request.form['email']
        session['password'] = hashlib.md5(request.form['password'].encode('utf-8')).hexdigest()
        return redirect(url_for('index'))


@app.route('/logout')
def logout():
    session.pop('email', None)
    session.pop('password', None)
    return redirect(url_for('index'))


@app.route('/confirm/<hashcode>')
def confirm(hashcode):
    user = User.query.filter_by(hashcode=hashcode).first()
    if user is None:
        return redirect(url_for('index'))
    user.hashcode = ''
    db.session.add(user)
    db.session.commit()
    session['email'] = user.email
    session['password'] = user.password
    return redirect(url_for('index'))


@app.route('/basket')
def basket():
    products = [
        {
            'id': 1,
            'count': 2
        },
        {
            'id': 1,
            'count': 2
        },
        {
            'id': 1,
            'count': 2
        }
    ]
    summa = 0
    for i in range(len(products)):
        prod = Product.query.filter_by(id=products[i]['id']).first()
        real_price = int(prod.price * (1 - prod.discount / 100))
        products[i] = [prod, real_price, products[i]['count']]
        summa += real_price * products[i][2]
    return render('basket.html', products=products, sum=summa)


@app.route('/lk-orders')
def lk_orders():
    return render('lk-orders.html')


@app.route('/lk-msg')
def lk_msg():
    return render('lk-msg.html')


@app.route('/lk-pass')
def lk_pass():
    return render('lk-pass.html')


@app.route('/manager-panel')
def manager_panel():
    return render('manager-panel.html')


@app.route('/category/<category>')
def category(category):
    cat = Category.query.filter_by(engname=category).first()
    products = cat.products[:]
    for i in range(len(products)):
        products[i] = [products[i], int(products[i].price * (1 - products[i].discount / 100))]
    return render('category.html', category=cat, products=products, len=len(products))


@app.route('/product/<int:id>')
def product(id):
    prod = Product.query.filter_by(id=id).first()
    real_price = int(prod.price * (1 - prod.discount / 100))
    return render('product.html', product=prod, real_price=real_price)
