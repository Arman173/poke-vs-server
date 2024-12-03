from flask import Blueprint, request, jsonify
from app.helpers.validations import pokemon_pd

# Crear el blueprint para pokemon
pokemon_blueprint = Blueprint('pokemon', __name__)

# Definir la ruta /pokemon que acepta POST
@pokemon_blueprint.route('/pokemon', methods=['GET'])
def combat():
    # Convertir usando la columna "Name" como llave
    json_data = pokemon_pd.set_index("Name").to_dict(orient="index")

    # Devolver el diccionario como respuesta JSON
    return jsonify(json_data)