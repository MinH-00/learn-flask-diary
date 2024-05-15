from flask import Blueprint, render_template, request

#create blueprint
auth = Blueprint('auth', __name__)

#route
#logout
@auth.route('/logout')
def logout():
    return render_template('logout.html')

#login
@auth.route('/sign-in', methods=['GET', 'POST'])
def sign_in():
    return render_template('sign_in.html', user="SemiCircle")

#sign-up
@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        # 데이터 확인
        data = request.form

        # form - input의 name 속성을 기준으로 가져오기
        email = request.form.get('email')
        nickname = request.form.get('nickname')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        # 유효성 검사
        if len(email) < 5 :
            pass
        elif len(nickname) < 2:
            pass
        elif password1 != password2 :
            pass
        elif len(password1) < 7:
            pass
        else:
            pass  # Create User -> DB

    return render_template('sign_up.html')

