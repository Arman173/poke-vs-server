from marshmallow import schema, ValidationError
from app.schemas.pokemonSchema import CombatSchema

def validate_combat_schema(data):
    combat_schema = CombatSchema()
    # Validar los datos usando el esquema
    try:
        validated_data = combat_schema.load(data)
    except ValidationError as err:
        return False, err
    
    return True, validated_data