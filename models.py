from app import db
from sqlalchemy.sql import func


class User(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(50), unique=False, nullable=False)
    unread = db.Column(db.Integer, default=0)
    role = db.Column(db.Integer, unique=False, nullable=False, default=1)
    hashcode = db.Column(db.String(50), unique=True)

    '''
        0 - banned
        1 - user
        2 - manager
        3 - admin
    '''

    def __repr__(self):
        return '<User {}>'.format(self.email)


class Category(db.Model):

    __tablename__ = 'category'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), unique=True)
    engname = db.Column(db.String(50), unique=True)
    shown = db.Column(db.Integer, default=1)


class Product(db.Model):

    __tablename__ = 'product'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), unique=False, nullable=False)
    description = db.Column(db.String(1000), unique=False)
    count = db.Column(db.Integer, default=0)
    delivery = db.Column(db.Integer, default=0)
    image_url = db.Column(db.String(70), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    discount = db.Column(db.Integer, default=0)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))

    category = db.relationship('Category', backref=db.backref('products', lazy=True))


class Message(db.Model):

    __tablename__ = 'message'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.DateTime(timezone=True), server_default=func.now())
    type = db.Column(db.Integer, default=1)
    message = db.Column(db.String(500), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    user = db.relationship('User', backref=db.backref('messages', lazy=True))


db.create_all()
'''
cat = Category.query.filter_by(id=1).first()
prod = Product(name='Тапочки домашние', description='Lorem ipsum dolor sit amet', count=100, delivery=0,
               image_url='http://asds.ru/1.jpg', price=2000, discount=50, category=cat)
db.session.add(prod)
db.session.commit()
'''
