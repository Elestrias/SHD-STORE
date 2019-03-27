from flask_mail import Message
from app import app, mail
from flask import render_template, session, request, redirect, url_for
from models import db, User
import hashlib
from config import *


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    elif request.method == 'POST':
        if request.form['email'] == '':
            return render_template('register.html', email_empty=True)
        if len(request.form['password']) < 6:
            return render_template('register.html', pass_empty=True)
        if request.form['password'] != request.form['rpassword']:
            return render_template('register.html', diff_pass=True)
        if not request.form.get('accept'):
            return render_template('register.html', no_accept=True)
        if User.query.filter_by(email=request.form['email']).first() is not None:
            return render_template('register.html', user_exists=True)
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
        return render_template('register.html', success=True)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        if request.form['email'] == '':
            return render_template('login.html', email_empty=True)
        if request.form['password'] == '':
            return render_template('login.html', pass_empty=True)
        user = User.query.filter_by(email=request.form['email']).first()
        if user is None:
            return render_template('login.html', bad_data=True)
        if user.password != hashlib.md5((SALT + request.form['password']).encode('utf-8')).hexdigest():
            return render_template('login.html', bad_data=True)
        if user.role == 0:
            return render_template('login.html', banned=True)
        if user.hashcode != '':
            return render_template('login.html', unactivated=True)
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
