from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail

MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = 'egorsbrodov@gmail.com'
MAIL_PASSWORD = 'sbrodov2002'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/shop'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'asjdbasidgausg7di73q783fad7fde'
db = SQLAlchemy(app)
app.config.from_object(__name__)
mail = Mail(app)
