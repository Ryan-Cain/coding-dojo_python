from flask import Flask, render_template, request, redirect
from users import User

app = Flask(__name__)

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

if __name__ == "__main__":
    app.run(debug=True)