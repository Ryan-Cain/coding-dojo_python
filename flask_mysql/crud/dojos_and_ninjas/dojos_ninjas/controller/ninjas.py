from dojos_ninjas import app
from flask import render_template, redirect, request
from dojos_ninjas.models.dojo import Dojo
from dojos_ninjas.models.ninja import Ninja

@app.route('/ninjas')
def add_ninja():
    dojos = Dojo.get_all_dojos()
    return render_template('add_ninja.html', dojos=dojos)


@app.route('/submit_add_ninja', methods=["POST"])
def submit_add_ninja():
    Ninja.add_ninja(request.form)
    show_dojo_page = '/show_dojo/' + request.form['dojo_location']
    return redirect(show_dojo_page)
