from auth import *
from lk import *
from cart import *
from product_system import *


@app.route('/')
@app.route('/index')
def index():
    return render('index.html')


@app.route('/api/register', methods=['GET'])
def register():
    if check_args(request.args, 'login', 'password'):
        login = request.args['login']
        password = request.args['password']
        if query('SELECT * FROM users WHERE `login`="{}"'.format(login), True):
            return generate_answer(False, error_code=3)
        if len(password) < 6:
            return generate_answer(False, error_code=9)
        query('INSERT INTO users (`login`, `password`) VALUES ("{}", "{}")'.format(login, myhash(password)))
        return generate_answer(True, {'token': get_token(login)})
    return generate_answer(False, error_code=2)


@app.route('/api/login', methods=['GET'])
def log_in():
    if check_args(request.args, 'login', 'password'):
        login = request.args['login']
        password = request.args['password']
        res = query('SELECT * FROM users WHERE `login`="{}"'.format(login), True)
        if not res:
            return generate_answer(False, error_code=4)
        user_pass = res[0][2]
        if myhash(password) != user_pass:
            return generate_answer(False, error_code=5)
        return generate_answer(True, {'token': get_token(login)})
    return generate_answer(False, error_code=2)


@app.route('/api/logout', methods=['GET'])
def logout():
    if check_args(request.args, 'token'):
        token = request.args['token']
        res = query('SELECT * FROM sessions WHERE `token`="{}"'.format(token), True)
        if not res:
            return generate_answer(False, error_code=6)
        query('DELETE FROM sessions WHERE `token`="{}"'.format(token))
        return generate_answer(True, {})
    return generate_answer(False, error_code=2)


@app.route('/api/tasks/create', methods=['GET'])
def create():
    if not check_args(request.args, 'token', 'name'):
        return generate_answer(False, error_code=2)
    token = request.args['token']
    name = request.args['name']
    description = ''
    user_id = check_token(token)
    if not user_id:

        return generate_answer(False, error_code=6)
    if check_args(request.args, 'description'):
        description = request.args['description']

    query('INSERT INTO tasks (`user_id`, `name`, `parent_id`, `description`, `priority`) VALUES ({}, "{}", {}, "{}", {})'
          .format(user_id, name, parent_id, description, priority))
    return generate_answer(True, {})
