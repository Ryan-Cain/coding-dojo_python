# Create a new Flask application
# Have the root route ("/") show a page with the form
# Have the "/result" route display the information from the form on a new HTML page
# Put the form data into session

from flask import Flask, session, redirect, render_template, request
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex()
print(app.secret_key)

@app.route('/')
def base_form():
    return render_template('/form.html')

@app.route('/process', methods=["POST"])
def submit_form():
    session.clear()
    session['name'] = request.form['name']
    session['dojo_location'] = request.form['dojo_location']
    session['fav_language'] = request.form['fav_language']
    session['comment'] = request.form['comment']
    return redirect('/result')

@app.route('/result')
def display_result():
    return render_template('/result.html')

if __name__ == "__main__":
    app.run(debug=True)