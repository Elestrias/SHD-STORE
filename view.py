from auth import *
from lk import *
from cart import *
from product_system import *
from manager_panel import *
from admin_panel import *


@app.route('/')
@app.route('/index')
def index():
    return render('index.html')
