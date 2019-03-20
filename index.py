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


@app.route('/main', methods=['GET', 'POST'])
def main_page():
    global user
    return '''<!doctype html>
<html lang="en">
  <head>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="">
    <meta name="author" content="">
    <link rel="icon" href="../../../../favicon.ico">

    <title>Carousel Template for Bootstrap</title>

    <link rel="canonical" href="https://getbootstrap.com/docs/4.0/examples/carousel/">

    <!-- Bootstrap core CSS -->
    <link href="../../dist/css/bootstrap.min.css" rel="stylesheet">

    <!-- Custom styles for this template -->
    <link href="carousel.css" rel="stylesheet">
  </head>
  <body>

    <header>
      <nav class="navbar navbar-expand-md navbar-dark fixed-top bg-dark">
        <a class="navbar-brand" href="#">Carousel</a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarCollapse" aria-controls="navbarCollapse" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarCollapse">
          <ul class="navbar-nav mr-auto">
            <li class="nav-item active">
              <a class="nav-link" href="#">Home <span class="sr-only">(current)</span></a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#">Link</a>
            </li>
            <li class="nav-item">
              <a class="nav-link disabled" href="#">Disabled</a>
            </li>
          </ul>
          <form class="form-inline mt-2 mt-md-0">
            <input class="form-control mr-sm-2" type="text" placeholder="Search" aria-label="Search">
            <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
          </form>
        </div>
      </nav>
    </header>

    <main role="main">

      <div id="myCarousel" class="carousel slide" data-ride="carousel">
        <ol class="carousel-indicators">
          <li data-target="#myCarousel" data-slide-to="0" class="active"></li>
          <li data-target="#myCarousel" data-slide-to="1"></li>
          <li data-target="#myCarousel" data-slide-to="2"></li>
        </ol>
        <div class="carousel-inner">
          <div class="carousel-item active">
            <img class="first-slide" src="data:image/gif;base64,R0lGODlhAQABAIAAAHd3dwAAACH5BAAAAAAALAAAAAABAAEAAAICRAEAOw==" alt="First slide">
            <div class="container">
              <div class="carousel-caption text-left">
                <h1>Example headline.</h1>
                <p>Cras justo odio, dapibus ac facilisis in, egestas eget quam. Donec id elit non mi porta gravida at eget metus. Nullam id dolor id nibh ultricies vehicula ut id elit.</p>
                <p><a class="btn btn-lg btn-primary" href="#" role="button">Sign up today</a></p>
              </div>
            </div>
          </div>
          <div class="carousel-item">
            <img class="second-slide" src="data:image/gif;base64,R0lGODlhAQABAIAAAHd3dwAAACH5BAAAAAAALAAAAAABAAEAAAICRAEAOw==" alt="Second slide">
            <div class="container">
              <div class="carousel-caption">
                <h1>Another example headline.</h1>
                <p>Пакет задач в яндекс лицее</p>
                <p><a class="btn btn-lg btn-primary" href="#" role="button">Learn more</a></p>
              </div>
            </div>
          </div>
          <div class="carousel-item">
            <img class="third-slide" src="data:image/gif;base64,R0lGODlhAQABAIAAAHd3dwAAACH5BAAAAAAALAAAAAABAAEAAAICRAEAOw==" alt="Third slide">
            <div class="container">
              <div class="carousel-caption text-right">
                <h1>One more for good measure.</h1>
                <p>Mac book Егора</p>
                <p><a class="btn btn-lg btn-primary" href="#" role="button">Browse gallery</a></p>
              </div>
            </div>
          </div>
        </div>
        <a class="carousel-control-prev" href="#myCarousel" role="button" data-slide="prev">
          <span class="carousel-control-prev-icon" aria-hidden="true"></span>
          <span class="sr-only">Previous</span>
        </a>
        <a class="carousel-control-next" href="#myCarousel" role="button" data-slide="next">
          <span class="carousel-control-next-icon" aria-hidden="true"></span>
          <span class="sr-only">Next</span>
        </a>
      </div>


      <!-- Marketing messaging and featurettes
      ================================================== -->
      <!-- Wrap the rest of the page in another container to center all the content. -->

      <div class="container marketing">

        <!-- Three columns of text below the carousel -->
        <div class="row">
          <div class="col-lg-4">
            <img class="rounded-circle" src="data:image/gif;base64,R0lGODlhAQABAIAAAHd3dwAAACH5BAAAAAAALAAAAAABAAEAAAICRAEAOw==" alt="Generic placeholder image" width="140" height="140">
            <h2>Тапки Руслана</h2>
            <p>Новые тапки от Рус-кож-пром-комбинат, натуральная кожа, отличное качество</p>
            <p><a class="btn btn-secondary" href="#" role="button">View details &raquo;</a></p>
          </div><!-- /.col-lg-4 -->
          <div class="col-lg-4">
            <img class="rounded-circle" src="data:image/gif;base64,R0lGODlhAQABAIAAAHd3dwAAACH5BAAAAAAALAAAAAABAAEAAAICRAEAOw==" alt="Generic placeholder image" width="140" height="140">
            <h2>Mac book Егора</h2>
            <p>Бесполезный кусок микросхемок и проводков, работает с пол пинка, нельзя играть в игры</p>
            <p><a class="btn btn-secondary" href="#" role="button">View details &raquo;</a></p>
          </div><!-- /.col-lg-4 -->
          <div class="col-lg-4">
            <img class="rounded-circle" src="data:image/gif;base64,R0lGODlhAQABAIAAAHd3dwAAACH5BAAAAAAALAAAAAABAAEAAAICRAEAOw==" alt="Generic placeholder image" width="140" height="140">
            <h2>Пакет задач и проектов Яндекс Лицей</h2>
            <p>Полный сборник всех-всех работ необходимых для успешного обучения (без труда) в Яндекс Лицее</p>
            <p><a class="btn btn-secondary" href="#" role="button">View details &raquo;</a></p>
          </div><!-- /.col-lg-4 -->
        </div><!-- /.row -->


        <!-- START THE FEATURETTES -->

        <hr class="featurette-divider">

        <div class="row featurette">
          <div class="col-md-7">
            <h2 class="featurette-heading">First featurette heading. <span class="text-muted">It'll blow your mind.</span></h2>
            <p class="lead">Donec ullamcorper nulla non metus auctor fringilla. Vestibulum id ligula porta felis euismod semper. Praesent commodo cursus magna, vel scelerisque nisl consectetur. Fusce dapibus, tellus ac cursus commodo.</p>
          </div>
          <div class="col-md-5">
            <img class="featurette-image img-fluid mx-auto" data-src="holder.js/500x500/auto" alt="Generic placeholder image">
          </div>
        </div>

        <hr class="featurette-divider">

        <div class="row featurette">
          <div class="col-md-7 order-md-2">
            <h2 class="featurette-heading">Oh yeah, it's that good. <span class="text-muted">See for yourself.</span></h2>
            <p class="lead">Donec ullamcorper nulla non metus auctor fringilla. Vestibulum id ligula porta felis euismod semper. Praesent commodo cursus magna, vel scelerisque nisl consectetur. Fusce dapibus, tellus ac cursus commodo.</p>
          </div>
          <div class="col-md-5 order-md-1">
            <img class="featurette-image img-fluid mx-auto" data-src="holder.js/500x500/auto" alt="Generic placeholder image">
          </div>
        </div>

        <hr class="featurette-divider">

        <div class="row featurette">
          <div class="col-md-7">
            <h2 class="featurette-heading">And lastly, this one. <span class="text-muted">Checkmate.</span></h2>
            <p class="lead">Donec ullamcorper nulla non metus auctor fringilla. Vestibulum id ligula porta felis euismod semper. Praesent commodo cursus magna, vel scelerisque nisl consectetur. Fusce dapibus, tellus ac cursus commodo.</p>
          </div>
          <div class="col-md-5">
            <img class="featurette-image img-fluid mx-auto" data-src="holder.js/500x500/auto" alt="Generic placeholder image">
          </div>
        </div>

        <hr class="featurette-divider">

        <!-- /END THE FEATURETTES -->

      </div><!-- /.container -->


      <!-- FOOTER -->
      <footer class="container">
        <p class="float-right"><a href="#">Back to top</a></p>
        <p>&copy; 2017-2018 Company, Inc. &middot; <a href="#">Privacy</a> &middot; <a href="#">Terms</a></p>
      </footer>
    </main>

    <!-- Bootstrap core JavaScript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script>window.jQuery || document.write('<script src="../../assets/js/vendor/jquery-slim.min.js"><\/script>')</script>
    <script src="../../assets/js/vendor/popper.min.js"></script>
    <script src="../../dist/js/bootstrap.min.js"></script>
    <!-- Just to make our placeholder images work. Don't actually copy the next line! -->
    <script src="../../assets/js/vendor/holder.min.js"></script>
  </body>
</html>
'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')


