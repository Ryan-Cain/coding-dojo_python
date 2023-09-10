from flask_app import app
from flask import render_template, request, redirect
from flask_app_users.models.user import User

@app.route('/')
def read_users():
    users = User.get_all_users()
    return render_template('/read_users.html', users=users)

@app.route('/create_user')
def create_user():
    return render_template('/create_user.html')

@app.route('/submit_new_user', methods=["POST"])
def submit_new_user():
    User.create_new_user(request.form)
    return redirect('/')

@app.route('/edit_user/<int:id>')
def edit_user(id):
    user = User.get_user(id)
    return render_template('/edit_user.html', user=user)

@app.route('/submit_edit_user', methods=["POST"])
def submit_edit_user():
    updateUserPath = '/show_user/' + request.form['id']
    User.edit_user(request.form)
    return redirect(updateUserPath)

@app.route('/show_user/<int:id>')
def show_user(id):
    user = User.get_user(id)
    return render_template('/show_user.html', user=user)

@app.route('/delete_user/<int:id>')
def delete_user(id):
    User.delete_user(id)
    return redirect('/')