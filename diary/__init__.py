from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#create DB connection
db = SQLAlchemy()
DB_NAME = "database.db"

# create App
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'semicircle_secret_key'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    #import Blueprint
    from .views import views
    from .auth import auth

    #Apply BluePrint
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')


    return app