from login_reg_app import app
from flask import render_template, redirect, request, session
from login_reg_app.models.registration import Registration
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def reg_login():
    return render_template('login_reg.html')

@app.route('/submit_registration', methods=["POST"])
def submit_registration():
    print(request.form)
    if not Registration.validated(request.form):
        return redirect('/')
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    userInfo = {
        **request.form,
        'password': pw_hash
    }
    user_id = Registration.register_user(userInfo)
    
    session['user_id'] = user_id
    session['first_name'] = request.form['first_name']

    return redirect('/logged_in')


