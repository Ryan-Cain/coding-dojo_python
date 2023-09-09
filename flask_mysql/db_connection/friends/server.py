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

@app.route('/get_friend_by_id/<int:id>')
def get_friend_by_id(id):
    friend = Friend.get_friend_by_id(id)
    return render_template('/single_friend.html', friend=friend)

@app.route('/update_friend/<int:id>')
def update_friend(id):
    friend = Friend.get_friend_by_id(id)
    return render_template('/update_friend.html', friend=friend)

@app.route('/update_friend_submit', methods=["POST"])
def update_friend_submit():
    Friend.update_friend(request.form)
    return redirect('/')

@app.route('/delete_friend/<int:id>')
def delete_friend_by_id(id):
    Friend.delete_friend(id)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)