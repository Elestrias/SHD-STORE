from flask import Flask, url_for, request, render_template

app = Flask(__name__)
user = 'Unknown'


@app.route('/registration', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return render_template('registration.html')
    elif request.method == 'POST':
            print(request.form['email'])
            print(request.form['password'])
            print(request.form['file'])
            print(request.form['about'])
            print(request.form['accept'])
            print(request.form['sex'])
            return "Форма отправлена"


@app.route('/login', methods=['GET', 'POST'])
def main_page():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        print(request.form['email'])
        print(request.form['password'])
        print(request.form['ld'])
        return "Добро пожаловать"


@app.route('/', methods=['POST', 'GET'])
@app.route('/main', methods=['POST', 'GET'])
def main():
    if request.method == 'GET':
        return render_template('main_page.html')
    elif request.method == 'POST':
            print(request.form['email'])
            print(request.form['password'])
            print(request.form['file'])
            print(request.form['about'])
            print(request.form['accept'])
            print(request.form['sex'])
            return "Форма отправлена"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
