from flask import Flask
from dojos_ninjas import app

from dojos_ninjas.controller import dojos
from dojos_ninjas.controller import ninjas

if __name__ == "__main__":
    app.run(debug=True)
