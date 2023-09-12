from login_reg_app import app
from flask import render_template, redirect, request, session, flash
from login_reg_app.models.login import Login
from login_reg_app.controllers.registrations import bcrypt

@app.route('/submit_login', methods=["POST"])
def submit_login():
    print(request.form)
    user = Login.user_exists(request.form['email'])
    if not user:
        flash('Invalid Email/Password', 'login')
        return redirect('/')
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash('Invalid Email/Password', 'login')
        return redirect('/')
    
    session['user_id'] = user.id
    session['first_name'] = user.first_name
    print("successfully logged in")
    return redirect('/logged_in')


@app.route('/logged_in')
def logged_in():
    if 'user_id' not in session:
        return redirect('/')
    return render_template('logged_in.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')