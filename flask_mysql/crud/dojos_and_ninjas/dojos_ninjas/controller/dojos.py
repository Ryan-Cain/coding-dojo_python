from dojos_ninjas import app
from flask import render_template, redirect, request

from dojos_ninjas.models.dojo import Dojo

@app.route('/')
def go_to_dojos():
    return redirect('/dojos')

@app.route('/dojos')
def dojos():
    dojos = Dojo.get_all_dojos()
    return render_template('dojos.html', dojos=dojos)

@app.route('/show_dojo/<int:id>')
def show_dojo(id):
    dojo = Dojo.get_single_dojo(id)
    return render_template('show_dojo.html', dojo=dojo)

@app.route('/add_dojo', methods=["POST"])
def add_dojo():
    Dojo.add_dojo_to_db(request.form)
    return redirect('/')