from auth import *
from lk import *
from cart import *
from product_system import *
from Models import *
from flask import request
from Adapters import check_args, generate_answer, \
    query, myhash, get_token, check_token, process_task_list, get_update_sql





@app.route('/')
@app.route('/index')
def index():
    return render('index.html')


@app.route('/api/register', methods=['GET'])
def register():
    if check_args(request.args, 'login', 'password'):
        login = request.args['login']
        password = request.args['password']
        if User.query.filter(User.email('{}')).all().format(login) > 0:
            return generate_answer(False, error_code=3)
        if len(password) < 6:
            return generate_answer(False, error_code=9)
        user = User(email=login,password=password)
        db.session.add(user)
        db.session.commit()
    return generate_answer(False, error_code=2)


@app.route('/api/login', methods=['GET'])
def log_in():
    if check_args(request.args, 'login', 'password'):
        login = request.args['login']
        password = request.args['password']
        user_pass = User.query.filter(User.email('{}')).first().format(login).password()
        if not user_pass:
            return generate_answer(False, error_code=4)
        if myhash(password) != user_pass:
            return generate_answer(False, error_code=5)
        db.session.add(User.filtered_by(email=login).first())
        return generate_answer(True, {'token': get_token(login)})
    return generate_answer(False, error_code=2)


@app.route('/api/logout', methods=['GET'])
def logout():
    if check_args(request.args, 'token'):
        token = request.args['token']
        res = query('SELECT * FROM sessions WHERE `token`="{}"'.format(token), True)
        if not res:
            return generate_answer(False, error_code=6)
        db.session.delete(User.filtered_by(email=login).first())
        return generate_answer(True, {})
    return generate_answer(False, error_code=2)


@app.route('/api/product/create', methods=['GET'])
def create():
    login = request.args['login']
    status = User.query.filtered_by(email=login).first().role()
    if status != 3 or status != 2:
        return generate_answer(False, error_code=13)
    if not check_args(request.args, 'token', 'name'):
        return generate_answer(False, error_code=2)
    token = request.args['token']
    name = request.args['name']
    description = request.args['description']
    price = request.args['price']
    cathegory = request.args['cathegory']
    user_id = User.query.filtered_by(email=login).first().id()
    if not user_id:
        return generate_answer(False, error_code=6)
    if check_args(request.args, 'description'):
        description = request.args['description']
    page = Product(name=name,description=description, price=price)
    db.session.add(page)
    db.commit()
    return generate_answer(True, {})


@app.route('api/product/delete', methods=['GET'])
def delete():
    login = request.args['login']
    status = User.query.filtered_by(email=login).first().role()
    if status != 3 or status != 2:
        return generate_answer(False, error_code=13)
    if not check_args(request.args, 'token', 'id'):
         return generate_answer(False, error_code=2)
    try:
        product_id = int(request.args['id'])
    except ValueError:
        return generate_answer(False, error_code=12)
    user_id = check_token(request.args['token'])
    if not user_id:
        return generate_answer(False, error_code=6)
    res = Product.query.filtered_by
    if not res:
        return generate_answer(False, error_code=13)
    query('DELETE FROM products WHERE `id`={0}'.format(product_id))
    return generate_answer(True, {})


@app.route('api/product/status', methods=['GET'])
def status():

