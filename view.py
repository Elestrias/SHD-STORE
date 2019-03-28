from auth import *
from lk import *
from cart import *
from product_system import *


@app.route('/')
@app.route('/index')
def index():
    return render('index.html')
