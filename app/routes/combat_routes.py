from flask import Blueprint, request, jsonify
import numpy as np
import tensorflow as tf
from app.helpers.helpers import normalize_tf
from app.helpers.validations import validate_combat_schema, getPokemonStadistic

# cargamos nuestro modelo
modelo = tf.keras.models.load_model('app/models/model.keras')

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
    name1 = validated_data.get('pkm1')
    name2 = validated_data.get('pkm2')

    found1, stadistic1_df = getPokemonStadistic(name1)
    found2, stadistic2_df = getPokemonStadistic(name2)

    # print(stadistic1, stadistic2)

    if not found1 or not found2:
        return jsonify({"errors": "No se encontraron las estadisticas de algun pokemon"}), 400
    
    # Procesamos las estadisticas para introducirlo en nuestra red
    columns = ['HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed', 'Legendary']
    stadistic1 = stadistic1_df[columns].to_numpy()
    stadistic2 = stadistic2_df[columns].to_numpy()

    diff = stadistic1 - stadistic2

    # obtenemos el factor de tipo
    types1 = [stadistic1_df['Type 1'], stadistic1_df['Type 2']]
    types2 = [stadistic2_df['Type 1'], stadistic2_df['Type 2']]
    ft = normalize_tf(types1, types2)
    diff = np.hstack((ft, diff))

    print(stadistic1, stadistic2, diff)

    # if not (stadistic1 and stadistic2):
    #     print(stadistic1, stadistic2)
    #     return jsonify({"errors": "No se encontraron las estadisticas de algun pokemon"}), 400

    # usamos nuestro modelo para predecir el resultado
    print('Entrada:', diff)
    predict = modelo.predict(np.array([diff], dtype=np.float32))
    print(predict)
    validated_data['winner'] = name1 if predict[0] >= 0.5 else name2
    
    # Devolver los datos pero con el resultado del que gano
    return jsonify({"received_data": validated_data}), 200
