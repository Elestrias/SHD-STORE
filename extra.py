from models import db, Message as Msg, User, Category
from flask import session, render_template

MESSAGE_NOTIFICATION = 1
MESSAGE_SUCCESS = 2
MESSAGE_ERROR = 3


def render(temp, **kwargs):
    return render_template(temp, categories=Category.query.filter_by(shown=1).all(), current_user=get_current_user(), **kwargs)


def update_db(obj):
    db.session.add(obj)
    db.session.commit()


def send_message(type, msg, user):
    user.unread += 1
    update_db(user)
    message = Msg(type=type, message=msg, user=user)
    update_db(message)


def get_current_user():
    if 'email' not in session:
        return None
    return User.query.filter_by(email=session['email']).first()
