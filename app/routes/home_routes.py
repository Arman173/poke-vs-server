from flask import Blueprint, render_template

# Definimos el blueprint
home_blueprint = Blueprint('home', __name__)

# Ruta principal
@home_blueprint.route("/")
def home():
    return render_template("index.html")
