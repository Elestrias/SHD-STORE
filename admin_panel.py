from app import app
from flask import redirect, url_for, request
from extra import *


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
