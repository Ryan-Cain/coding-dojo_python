# Create a root route ("/") that responds with "Hello World!"
# Create a route that responds with "Dojo!"
# Create a route that responds with "Hi" and whatever name is in the URL after /say/
# Create a route that responds with the given word repeated as many times as specified in the URL
# NINJA BONUS: Ensure the names provided in the 3rd task are strings
# NINJA BONUS: For the 4th task, ensure the 2nd element in the URL is an integer, and the 3rd element is a string
# SENSEI BONUS: Ensure that if the user types in any route other than the ones specified, they receive an error message saying "Sorry! No response. Try again."


from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/dojo')
def dojo():
    return 'Dojo!'

@app.route('/say/<string:name>')
def say_name(name):
    newName = name.capitalize()
    return f'Hi {newName}!'

@app.route('/repeat/<int:num>/<string:name>')
def repeat(num, name):
    return name*num

@app.errorhandler(404)
def page_not_found(e):
    return "Sorry! No response. Try again."

if __name__=='__main__':
    app.run(debug=True)