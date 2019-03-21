from flask_restful import abort

from flask import Flask, redirect, session, request
from flask import render_template as flask_render_template



def init_route(app, db):

    def render_template(*args, **kwargs):
        kwargs['auth_user'] = auth.get_user()
        return flask_render_template(*args, **kwargs)

    init_api_v1(app, auth)

    @app.route('/')
    @app.route('/index')
    def index():
        if not auth.is_authorized():
            return render_template(
                'login.html',
                title='Главная',
            )
        main_page = News.query.filter_by(user_id=auth.get_user().id)
        return render_template(
            'main.html',
            title="Главная",
            products_list=products_list
        )

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        has_error = False
        login = ''
        if request.method == 'POST':
            username = request.form['username']
            if auth.login(username, request.form['password']):
                return redirect('/')
            else:
                has_error = True
        return render_template(
            'login.html',
            title='Вход',
            login=login,
            has_error=has_error
        )

    @app.route('/logout', methods=['GET'])
    def logout():
        auth.logout()
        return redirect('/')

    @app.route('/user/create', methods=['GET', 'POST'])
    def registration():
        has_error = False
        form = UserCreateForm()
        if form.validate_on_submit():
            username = form.username.data
            password = form.password.data
            user = User.query.filter_by(username=username).first()
            if user:
                has_error = True
            else:
                User.add(username=username, password=password)
                auth.login(username, password)
                return redirect('/')
        return render_template(
            'registration.html',
            title='Зарегистрироваться',
            form=form,
            has_error=has_error
        )

    @app.route('/products', methods=['GET'])
    def news_list():
        if not auth.is_authorized():
            return redirect('/login')
        news_list = News.query.filter_by(user_id=auth.get_user().id)
        return render_template(
            'product-list.html',
            title="Товар",
            news_list=news_list
        )

    @app.route('/products/create', methods=['GET', 'POST'])
    def news_create_form():
        if not auth.is_authorized():
            return redirect('/login')
        form = ProductsCreateForm()
        if form.validate_on_submit():
            title = form.title.data
            content = form.content.data
            Products.add(title=title, content=content, user=auth.get_user())
            return redirect('/')
        return render_template(
            'news-create.html',
            title='Создать stuff_page',
            form=form
        )

    @app.route('/products/<int:id>')
    def news_view(id: int):
        if not auth.is_authorized():
            return redirect('/login')
        news = Products.query.filter_by(id=id).first()
        if not news:
            abort(404)
        if news.user_id != auth.get_user().id:
            abort(403)
        user = news.user
        return render_template(
            'news-view.html',
            title=news.title,
            product=product,
            user=user
        )

    @app.route('/products/delete/<int:id>')
    def news_delete(id: int):
        if not auth.is_authorized():
            return redirect('/login')
        news = Products.query.filter_by(id=id).first()
        if news.user_id != auth.get_user().id:
            abort(403)
        Products.delete(news)
        return redirect('/products')
