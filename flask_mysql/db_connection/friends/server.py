from flask import Flask, render_template, redirect, request
from friend import Friend


app = Flask(__name__)

@app.route('/')
def friends():
    friends = Friend.get_all()
    return render_template('index.html', friends=friends)

@app.route('/add_friend')
def add_friend():
    return render_template('add_friend.html')

@app.route('/add_friend_submit', methods=["POST"])
def add_friend_form_submit():
 
    Friend.save(request.form)
    return redirect('/')

@app.route('/get_friend_by_id/<int:num>')
def get_friend_by_id(num):
    friend = Friend.get_friend_by_id(num)
    return render_template('/single_friend.html', friend=friend)

# @app.route('/update_record')
# def update_record():

#     return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)