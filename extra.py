import hashlib
from models import db, Message as Msg, User, Category, Product
from flask import session, render_template
from config import *

MESSAGE_NOTIFICATION = 1
MESSAGE_SUCCESS = 2
MESSAGE_ERROR = 3


def render(temp, **kwargs):
    return render_template(temp, categories=Category.query.filter_by(shown=1).all(), current_user=get_current_user(), **kwargs)


def update_db(obj):
    db.session.add(obj)
    db.session.commit()
    db.session.flush()


def send_message(type, msg, user):
    user.unread += 1
    update_db(user)
    message = Msg(type=type, message=msg, user=user)
    update_db(message)


def get_current_user():
    if 'email' not in session:
        return None
    return User.query.filter_by(email=session['email']).first()


def get_real_price(products):
    summa = 0
    for pr in products:
        product = Product.query.filter_by(id=pr['id']).first()
        summa += int(product.price * (1 - product.discount / 100) * pr['count'] + product.delivery)
    return summa


def get_predesc(products):
    items = []
    for prod in products:
        items.append(Product.query.filter_by(id=prod['id']).first().name)
    res = ', '.join(items)
    if len(res) <= 25:
        return res
    return ', '.join(items)[:25] + '...'


def hash_password(password):
    return hashlib.md5((SALT + password).encode('utf-8')).hexdigest()
