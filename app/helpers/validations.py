import pandas as pd
from marshmallow import schema, ValidationError
from app.schemas.pokemonSchema import CombatSchema
from app.helpers.helpers import preprocess_pokemon_data, normalize_columns

pokemon_pd = pd.read_csv('app/databases/pokemon.csv')
pokemon_pd = preprocess_pokemon_data(pokemon_pd)
pokemon_pd['Name'] = pokemon_pd['Name'].str.lower()

# Normalizamos los datos (estadisticas) en un rango de [-10.0, 10.0]
# columns_to_normalize = ["HP","Attack","Defense","Sp. Atk","Sp. Def","Speed","Legendary"]
# pokemon_pd = normalize_columns(pokemon_pd, columns_to_normalize, min_val=-10.0, max_val=10.0)

def validate_combat_schema(data):
    combat_schema = CombatSchema()
    # Validar los datos usando el esquema
    try:
        validated_data = combat_schema.load(data)
    except ValidationError as err:
        return False, err
    
    return True, validated_data

# Función que devuelve las estadisticas de un pokemon por su nombre
def getPokemonStadistic(name: str):
    print(pokemon_pd.head())
    if name not in pokemon_pd['Name'].values:
        print('No esta el pokemon',name,'en nuestra base de datos...')
        return False, None
    
    index = pokemon_pd[pokemon_pd['Name'] == name].index[0]
    return True, pokemon_pd.loc[index]