from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

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

    #Create or Import Database
    from .models import User, Note
    create_database(app)


    return app

#Create or Check
def create_database(app):
    # db파일이 확인안될 때만 생성
    if not path.exists('website/' + DB_NAME):
        with app.app_context():
            db.create_all()
        print('>>> Create DB')