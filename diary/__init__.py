from flask import Flask

# create App
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'semicircle_secret_key'

    #import Blueprint
    from .views import views
    from .auth import auth

    #Apply BluePrint
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')


    return app