from flask import Flask, url_for, request, render_template

app = Flask(__name__)
user = 'Unknown'


@app.route('/', methods=['POST', 'GET'])
def form_sample():
    global user
    if request.method == 'GET':
        return '''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport"
                            content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
                            integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm"
                            crossorigin="anonymous">
                            <title>Пример формы</title>
                          </head>
                          <body>
                            <h1>Регистрация SHDstore</h1>
                            <form method="post">
                                <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                <input type="password" class="form-control" id="password" placeholder="Введите пароль" name="password">
                                
                                <div class="form-group">
                                    <label for="about">Платежная информация</label>
                                    <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                </div>
                                <div class="form-group">
                                    <label for="photo">Приложите фотографию</label>
                                    <input type="file" class="form-control-file" id="photo" name="file">
                                </div>
                                <div class="form-group">
                                    <label for="form-check">Укажите пол</label>
                                    <div class="form-check">
                                      <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                      <label class="form-check-label" for="male">
                                        Мужской
                                      </label>
                                    </div>
                                    <div class="form-check">
                                      <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                      <label class="form-check-label" for="female">
                                        Женский
                                      </label>
                                    </div>
                                </div>
                                <div class="form-group form-check">
                                    <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                    <label class="form-check-label" for="acceptRules">согласен с условиями пользования</label>
                                </div>
                                <button type="submit" class="btn btn-primary">Записаться</button>
                            </form>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        user = request.form['email']
        password = request.form['password']
        avatar = request.form['file']
        info = request.form['about']
        accepted = request.form['accept']
        sex = request.form['sex']
        return "Форма отправлена"\



@app.route('/payment_information', methods=['GET', 'POST'])
def index():
    global user
    return render_template('index.html', title='Домашняя страница',
                           username=user), '''<!doctype html>
                                    <html lang="en">
                                      <head>
                                            <div class="col-md-8 order-md-1">
                                              <h4 class="mb-3">Billing address</h4>
                                              <form class="needs-validation" novalidate>
                                                <div class="row">
                                                  <div class="col-md-6 mb-3">
                                                    <label for="firstName">First name</label>
                                                    <input type="text" class="form-control" id="firstName" placeholder="" value="" required>
                                                    <div class="invalid-feedback">
                                                      Valid first name is required.
                                                    </div>
                                                  </div>
                                                  <div class="col-md-6 mb-3">
                                                    <label for="lastName">Last name</label>
                                                    <input type="text" class="form-control" id="lastName" placeholder="" value="" required>
                                                    <div class="invalid-feedback">
                                                      Valid last name is required.
                                                    </div>
                                                  </div>
                                                </div>
                                    
                                                <div class="mb-3">
                                                  <label for="username">Username</label>
                                                  <div class="input-group">
                                                    <div class="input-group-prepend">
                                                      <span class="input-group-text">@</span>
                                                    </div>
                                                    <input type="text" class="form-control" id="username" placeholder="Username" required>
                                                    <div class="invalid-feedback" style="width: 100%;">
                                                      Your username is required.
                                                    </div>
                                                  </div>
                                                </div>
                                    
                                                <div class="mb-3">
                                                  <label for="email">Email <span class="text-muted">(Optional)</span></label>
                                                  <input type="email" class="form-control" id="email" placeholder="you@example.com">
                                                  <div class="invalid-feedback">
                                                    Please enter a valid email address for shipping updates.
                                                  </div>
                                                </div>
                                    
                                                <div class="mb-3">
                                                  <label for="address">Address</label>
                                                  <input type="text" class="form-control" id="address" placeholder="1234 Main St" required>
                                                  <div class="invalid-feedback">
                                                    Please enter your shipping address.
                                                  </div>
                                                </div>
                                    
                                                <div class="mb-3">
                                                  <label for="address2">Address 2 <span class="text-muted">(Optional)</span></label>
                                                  <input type="text" class="form-control" id="address2" placeholder="Apartment or suite">
                                                </div>
                                    
                                                <div class="row">
                                                  <div class="col-md-5 mb-3">
                                                    <label for="country">Country</label>
                                                    <select class="custom-select d-block w-100" id="country" required>
                                                      <option value="">Choose...</option>
                                                      <option>United States</option>
                                                    </select>
                                                    <div class="invalid-feedback">
                                                      Please select a valid country.
                                                    </div>
                                                  </div>
                                                  <div class="col-md-4 mb-3">
                                                    <label for="state">State</label>
                                                    <select class="custom-select d-block w-100" id="state" required>
                                                      <option value="">Choose...</option>
                                                      <option>California</option>
                                                    </select>
                                                    <div class="invalid-feedback">
                                                      Please provide a valid state.
                                                    </div>
                                                  </div>
                                                  <div class="col-md-3 mb-3">
                                                    <label for="zip">Zip</label>
                                                    <input type="text" class="form-control" id="zip" placeholder="" required>
                                                    <div class="invalid-feedback">
                                                      Zip code required.
                                                    </div>
                                                  </div>
                                                </div>
                                                <hr class="mb-4">
                                                <div class="custom-control custom-checkbox">
                                                  <input type="checkbox" class="custom-control-input" id="same-address">
                                                  <label class="custom-control-label" for="same-address">Shipping address is the same as my billing address</label>
                                                </div>
                                                <div class="custom-control custom-checkbox">
                                                  <input type="checkbox" class="custom-control-input" id="save-info">
                                                  <label class="custom-control-label" for="save-info">Save this information for next time</label>
                                                </div>
                                                <hr class="mb-4">
                                    
                                                <h4 class="mb-3">Payment</h4>
                                    
                                                <div class="d-block my-3">
                                                  <div class="custom-control custom-radio">
                                                    <input id="credit" name="paymentMethod" type="radio" class="custom-control-input" checked required>
                                                    <label class="custom-control-label" for="credit">Credit card</label>
                                                  </div>
                                                  <div class="custom-control custom-radio">
                                                    <input id="debit" name="paymentMethod" type="radio" class="custom-control-input" required>
                                                    <label class="custom-control-label" for="debit">Debit card</label>
                                                  </div>
                                                  <div class="custom-control custom-radio">
                                                    <input id="paypal" name="paymentMethod" type="radio" class="custom-control-input" required>
                                                    <label class="custom-control-label" for="paypal">Paypal</label>
                                                  </div>
                                                </div>
                                                <div class="row">
                                                  <div class="col-md-6 mb-3">
                                                    <label for="cc-name">Name on card</label>
                                                    <input type="text" class="form-control" id="cc-name" placeholder="" required>
                                                    <small class="text-muted">Full name as displayed on card</small>
                                                    <div class="invalid-feedback">
                                                      Name on card is required
                                                    </div>
                                                  </div>
                                                  <div class="col-md-6 mb-3">
                                                    <label for="cc-number">Credit card number</label>
                                                    <input type="text" class="form-control" id="cc-number" placeholder="" required>
                                                    <div class="invalid-feedback">
                                                      Credit card number is required
                                                    </div>
                                                  </div>
                                                </div>
                                                <div class="row">
                                                  <div class="col-md-3 mb-3">
                                                    <label for="cc-expiration">Expiration</label>
                                                    <input type="text" class="form-control" id="cc-expiration" placeholder="" required>
                                                    <div class="invalid-feedback">
                                                      Expiration date required
                                                    </div>
                                                  </div>
                                                  <div class="col-md-3 mb-3">
                                                    <label for="cc-expiration">CVV</label>
                                                    <input type="text" class="form-control" id="cc-cvv" placeholder="" required>
                                                    <div class="invalid-feedback">
                                                      Security code required
                                                    </div>
                                                  </div>
                                                </div>
                                                <hr class="mb-4">
                                                <button class="btn btn-primary btn-lg btn-block" type="submit">Continue to checkout</button>
                                              </form>
                                            </div>
                                          </div>
                                    
                                          <footer class="my-5 pt-5 text-muted text-center text-small">
                                            <p class="mb-1">&copy; 2017-2018 Company Name</p>
                                            <ul class="list-inline">
                                              <li class="list-inline-item"><a href="#">Privacy</a></li>
                                              <li class="list-inline-item"><a href="#">Terms</a></li>
                                              <li class="list-inline-item"><a href="#">Support</a></li>
                                            </ul>
                                          </footer>
                                        </div>
                                    
                                        <!-- Bootstrap core JavaScript
                                        ================================================== -->
                                        <!-- Placed at the end of the document so the pages load faster -->
                                        <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
                                        <script>window.jQuery || document.write('<script src="../../assets/js/vendor/jquery-slim.min.js"><\/script>')</script>
                                        <script src="../../assets/js/vendor/popper.min.js"></script>
                                        <script src="../../dist/js/bootstrap.min.js"></script>
                                        <script src="../../assets/js/vendor/holder.min.js"></script>
                                        <script>
                                          // Example starter JavaScript for disabling form submissions if there are invalid fields
                                          (function() {
                                            'use strict';
                                    
                                            window.addEventListener('load', function() {
                                              // Fetch all the forms we want to apply custom Bootstrap validation styles to
                                              var forms = document.getElementsByClassName('needs-validation');
                                    
                                              // Loop over them and prevent submission
                                              var validation = Array.prototype.filter.call(forms, function(form) {
                                                form.addEventListener('submit', function(event) {
                                                  if (form.checkValidity() === false) {
                                                    event.preventDefault();
                                                    event.stopPropagation();
                                                  }
                                                  form.classList.add('was-validated');
                                                }, false);
                                              });
                                            }, false);
                                          })();
                                        </script>
                                      </body>
                                    </html>'''


@app.route('/payment_information', methods=['GET', 'POST'])
def main():
    global user


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')


