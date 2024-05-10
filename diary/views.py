from flask import Blueprint

#create blueprint
views = Blueprint('views', __name__)

#route
@views.route('/sign-up')
def sign_up():
    return ('<h1>sign-up</h1>')
