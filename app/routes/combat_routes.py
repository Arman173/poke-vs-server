from flask import Blueprint, request, jsonify
from app.helpers.validations import validate_combat_schema

# Crear el blueprint para combat
combat_blueprint = Blueprint('combat', __name__)

# Definir la ruta /combat que acepta POST
@combat_blueprint.route('/combat', methods=['POST'])
def combat():
    # Obtener datos enviados por POST
    data = request.get_json()  # Leer JSON del cuerpo de la solicitud
    print(data)
    if not data:
        return jsonify({"error": "No se enviaron datos"}), 400
    
    
    # verificamos los datos

    # validated_data: contiene errores de validacion si ok = False
    ok, validated_data = validate_combat_schema(data)

    if not ok:
        return jsonify({"errors": validated_data.messages}), 400
    

    # verificamos si los pokemon son validos

    # usamos nuestro modelo para predecir el resultado
    
    # Devolver los datos pero con el resultado del que gano
    return jsonify({"received_data": data}), 200
