import os
import random

from flask import redirect, url_for, request

from app import app
from extra import *
from models import Order


@app.route('/change_status/<int:user_id>', methods=['GET', 'POST'])
def change_status(user_id):
    if 'email' not in session:
        return redirect(url_for('index'))
    if get_current_user().role < 3:
        return redirect(url_for('index'))
    if request.method == 'GET':
        return render('change-status.html', user_id=user_id)
    else:
        user = User.query.filter_by(id=user_id).first()
        if user.role < int(request.form['status']):
            send_message(MESSAGE_SUCCESS, 'Вас повысили', user)
        else:
            send_message(MESSAGE_ERROR, 'Вас понизили', user)
        user.role = int(request.form['status'])
        update_db(user)
        return redirect(url_for('user_info', user_id=user_id))


@app.route('/admin')
def admin():
    if 'email' not in session:
        return redirect(url_for('index'))
    if get_current_user().role < 3:
        return redirect(url_for('index'))
    count_orders = len(Order.query.all())
    count_users = len(User.query.all())
    count_products = len(Product.query.all())
    count_managers = len(User.query.filter_by(role=2).all())
    return render('admin.html', count_managers=count_managers, count_orders=count_orders,
                  count_products=count_products, count_users=count_users)


@app.route('/admin-products')
def admin_products():
    if 'email' not in session:
        return redirect(url_for('index'))
    if get_current_user().role < 3:
        return redirect(url_for('index'))
    products = Product.query.all()
    res = []
    for prod in products:
        res.append([prod, prod.price * (1 - prod.discount / 100)])
    return render('admin-products.html', products=res)


@app.route('/admin-categories')
def admin_categories():
    if 'email' not in session:
        return redirect(url_for('index'))
    if get_current_user().role < 3:
        return redirect(url_for('index'))
    cats = Category.query.all()
    return render('admin-categories.html', cats=cats)


@app.route('/admin-users')
def admin_users():
    if 'email' not in session:
        return redirect(url_for('index'))
    if get_current_user().role < 3:
        return redirect(url_for('index'))
    users = User.query.all()
    return render('admin-users.html', users=users)


@app.route('/add-product', methods=['GET', 'POST'])
def add_product():
    if 'email' not in session:
        return redirect(url_for('index'))
    if get_current_user().role < 3:
        return redirect(url_for('index'))
    if request.method == 'GET':
        return render('add-product.html', cats=Category.query.all())
    else:
        uploads_dir = os.path.join('/'.join(app.instance_path.split('/')[:-1]), 'static/upload_img')
        image = request.files['prod_image']
        ext = image.filename.split('.')[-1].lower()
        image_url = hash_password(request.form['prod_name'] + str(random.randint(1, 999))) + '.' + ext
        image.save(os.path.join(uploads_dir, image_url))
        product = Product(name=request.form['prod_name'],
                          description=request.form['prod_description'],
                          count=int(request.form['prod_count']),
                          delivery=int(request.form['prod_delivery']),
                          price=int(request.form['prod_price']),
                          discount=int(request.form['prod_discount']),
                          category=Category.query.filter_by(id=int(request.form['prod_category'])).first(),
                          image_url=image_url)
        update_db(product)
        return redirect(url_for('admin_products'))


@app.route('/edit-product/<int:id>', methods=['GET', 'POST'])
def edit_product(id):
    if 'email' not in session:
        return redirect(url_for('index'))
    if get_current_user().role < 3:
        return redirect(url_for('index'))
    if request.method == 'GET':
        product = Product.query.filter_by(id=id).first()
        return render('edit-product.html', cats=Category.query.all(), product=product)
    else:
        product = Product.query.filter_by(id=id).first()
        if request.files.get('prod_image') is not None:
            uploads_dir = os.path.join('/'.join(app.instance_path.split('/')[:-1]), 'static/upload_img')
            image = request.files['prod_image']

            ext = image.filename.split('.')[-1].lower()
            image_url = hash_password(request.form['prod_name'] + str(random.randint(1, 999))) + '.' + ext
            image.save(os.path.join(uploads_dir, image_url))
            product.image_url = image_url
        product.name = request.form['prod_name']
        product.description = request.form['prod_description']
        product.count = int(request.form['prod_count'])
        product.delivery = int(request.form['prod_delivery'])
        product.price = int(request.form['prod_price'])
        product.discount = int(request.form['prod_discount'])
        product.category = Category.query.filter_by(id=int(request.form['prod_category'])).first()
        update_db(product)
        return redirect(url_for('admin_products'))


@app.route('/delete-product/<int:id>')
def delete_product(id):
    if 'email' not in session:
        return redirect(url_for('index'))
    if get_current_user().role < 3:
        return redirect(url_for('index'))
    product = Product.query.filter_by(id=id).first()
    db.session.delete(product)
    db.session.commit()
    return redirect(url_for('admin_products'))


@app.route('/add-category', methods=['GET', 'POST'])
def add_category():
    if 'email' not in session:
        return redirect(url_for('index'))
    if get_current_user().role < 3:
        return redirect(url_for('index'))
    if request.method == 'GET':
        return render('add-category.html')
    else:
        cat = Category(name=request.form['cat_name'],
                       engname=request.form['cat_engname'],
                       shown=1 if bool(request.form.get('cat_shown')) else 0)
        update_db(cat)
        return redirect(url_for('admin_categories'))


@app.route('/edit-category/<int:id>', methods=['GET', 'POST'])
def edit_category(id):
    if 'email' not in session:
        return redirect(url_for('index'))
    if get_current_user().role < 3:
        return redirect(url_for('index'))
    if request.method == 'GET':
        cat = Category.query.filter_by(id=id).first()
        return render('edit-category.html', cat=cat)
    else:
        cat = Category.query.filter_by(id=id).first()
        cat.name = request.form['cat_name']
        cat.engname = request.form['cat_engname']
        cat.shown = 1 if bool(request.form.get('cat_shown')) else 0
        update_db(cat)
        return redirect(url_for('admin_categories'))


@app.route('/delete-category/<int:id>')
def delete_category(id):
    if 'email' not in session:
        return redirect(url_for('index'))
    if get_current_user().role < 3:
        return redirect(url_for('index'))
    cat = Category.query.filter_by(id=id).first()
    products = Product.query.filter_by(category=cat).all()
    for prod in products:
        db.session.delete(prod)
        db.session.commit()
    db.session.delete(cat)
    db.session.commit()
    return redirect(url_for('admin_categories'))
