# Create a new Flask project
# Have the /play route render a template with 3 blue boxes
# Have the /play/<x> route render a template with x number of blue boxes
# Have the /play/<x>/<color> route render a template with x number of boxes the color of the provided value
# NINJA BONUS: Use only one template for the whole project

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/play')
def play():
    return render_template('index.html', number=1, color='dodgerblue')

@app.route('/play/<int:num>')
def play_num(num):
    return render_template('index.html', number=num, color='dodgerblue')

@app.route('/play/<int:num>/<string:color>')
def play_num_color(num, color):
    return render_template('index.html', number=num, color=color)

if __name__ == "__main__":
    app.run(debug=True)