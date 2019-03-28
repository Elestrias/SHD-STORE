from app import app, mail
from flask import request, redirect, url_for
from extra import *
import hashlib
from config import *
from flask_mail import Message


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
        update_db(user)
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
    update_db(user)
    session['email'] = user.email
    session['password'] = user.password
    send_message(MESSAGE_SUCCESS, 'Вам успешно зачислено 100 бонусов за регистрацию', user)
    return redirect(url_for('index'))
