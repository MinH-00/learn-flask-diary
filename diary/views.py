from flask import Blueprint, render_template

#create blueprint
views = Blueprint('views', __name__)

#route
@views.route('/')
def sign_up():
    return render_template('home.html')
