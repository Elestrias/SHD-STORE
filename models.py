from app import db
from sqlalchemy.sql import expression


class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(50), unique=False, nullable=False)
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


db.create_all()
