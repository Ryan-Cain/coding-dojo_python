# Start a new Flask project
# Create a route in which the data above is declared and then sent to the template engine to be rendered
# Create the template that displays the data in a table
# NINJA BONUS: Use a framework to format the table

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def base_route():
    usersList = [
   {'first_name' : 'Michael', 'last_name' : 'Choi'},
   {'first_name' : 'John', 'last_name' : 'Supsupin'},
   {'first_name' : 'Mark', 'last_name' : 'Guillen'},
   {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
    return render_template('index.html', users=usersList)

if __name__ == "__main__":
    app.run(debug=True)