import pandas as pd

# Diccionario de efectividad de tipos (Generación 8)
type_chart = {
    "Normal": {"Normal": 1, "Fire": 1, "Water": 1, "Grass": 1, "Electric": 1, "Ice": 1, "Fighting": 2, "Poison": 1, "Ground": 1, "Flying": 1, "Psychic": 1, "Bug": 1, "Rock": 0.5, "Ghost": 0, "Dragon": 1, "Dark": 1, "Steel": 0.5, "Fairy": 1, "None": 0},
    "Fire": {"Normal": 1, "Fire": 0.5, "Water": 0.5, "Grass": 2, "Electric": 1, "Ice": 2, "Fighting": 1, "Poison": 1, "Ground": 1, "Flying": 1, "Psychic": 1, "Bug": 2, "Rock": 0.5, "Ghost": 1, "Dragon": 0.5, "Dark": 1, "Steel": 2, "Fairy": 1, "None": 0},
    "Water": {"Normal": 1, "Fire": 2, "Water": 0.5, "Grass": 0.5, "Electric": 1, "Ice": 1, "Fighting": 1, "Poison": 1, "Ground": 2, "Flying": 1, "Psychic": 1, "Bug": 1, "Rock": 2, "Ghost": 1, "Dragon": 0.5, "Dark": 1, "Steel": 1, "Fairy": 1, "None": 0},
    "Grass": {"Normal": 1, "Fire": 0.5, "Water": 2, "Grass": 0.5, "Electric": 1, "Ice": 1, "Fighting": 1, "Poison": 0.5, "Ground": 2, "Flying": 0.5, "Psychic": 1, "Bug": 0.5, "Rock": 2, "Ghost": 1, "Dragon": 0.5, "Dark": 1, "Steel": 0.5, "Fairy": 1, "None": 0},
    "Electric": {"Normal": 1, "Fire": 1, "Water": 2, "Grass": 0.5, "Electric": 0.5, "Ice": 1, "Fighting": 1, "Poison": 1, "Ground": 0, "Flying": 2, "Psychic": 1, "Bug": 1, "Rock": 1, "Ghost": 1, "Dragon": 0.5, "Dark": 1, "Steel": 1, "Fairy": 1, "None": 0},
    "Ice": {"Normal": 1, "Fire": 0.5, "Water": 0.5, "Grass": 2, "Electric": 1, "Ice": 0.5, "Fighting": 1, "Poison": 1, "Ground": 2, "Flying": 2, "Psychic": 1, "Bug": 1, "Rock": 1, "Ghost": 1, "Dragon": 2, "Dark": 1, "Steel": 0.5, "Fairy": 1, "None": 0},
    "Fighting": {"Normal": 2, "Fire": 1, "Water": 1, "Grass": 1, "Electric": 1, "Ice": 2, "Fighting": 1, "Poison": 0.5, "Ground": 1, "Flying": 0.5, "Psychic": 0.5, "Bug": 0.5, "Rock": 2, "Ghost": 0, "Dragon": 1, "Dark": 2, "Steel": 2, "Fairy": 0.5, "None": 0},
    "Poison": {"Normal": 1, "Fire": 1, "Water": 1, "Grass": 2, "Electric": 1, "Ice": 1, "Fighting": 1, "Poison": 0.5, "Ground": 0.5, "Flying": 1, "Psychic": 1, "Bug": 1, "Rock": 0.5, "Ghost": 0.5, "Dragon": 1, "Dark": 1, "Steel": 0, "Fairy": 2, "None": 0},
    "Ground": {"Normal": 1, "Fire": 2, "Water": 1, "Grass": 0.5, "Electric": 2, "Ice": 1, "Fighting": 1, "Poison": 2, "Ground": 1, "Flying": 0, "Psychic": 1, "Bug": 0.5, "Rock": 2, "Ghost": 1, "Dragon": 1, "Dark": 1, "Steel": 2, "Fairy": 1, "None": 0},
    "Flying": {"Normal": 1, "Fire": 1, "Water": 1, "Grass": 2, "Electric": 0.5, "Ice": 1, "Fighting": 2, "Poison": 1, "Ground": 1, "Flying": 1, "Psychic": 1, "Bug": 2, "Rock": 0.5, "Ghost": 1, "Dragon": 1, "Dark": 1, "Steel": 0.5, "Fairy": 1, "None": 0},
    "Psychic": {"Normal": 1, "Fire": 1, "Water": 1, "Grass": 1, "Electric": 1, "Ice": 1, "Fighting": 2, "Poison": 2, "Ground": 1, "Flying": 1, "Psychic": 0.5, "Bug": 1, "Rock": 1, "Ghost": 1, "Dragon": 1, "Dark": 0, "Steel": 0.5, "Fairy": 1, "None": 0},
    "Bug": {"Normal": 1, "Fire": 0.5, "Water": 1, "Grass": 2, "Electric": 1, "Ice": 1, "Fighting": 0.5, "Poison": 0.5, "Ground": 1, "Flying": 0.5, "Psychic": 2, "Bug": 1, "Rock": 1, "Ghost": 0.5, "Dragon": 1, "Dark": 2, "Steel": 0.5, "Fairy": 0.5, "None": 0},
    "Rock": {"Normal": 1, "Fire": 2, "Water": 1, "Grass": 1, "Electric": 1, "Ice": 2, "Fighting": 0.5, "Poison": 1, "Ground": 0.5, "Flying": 2, "Psychic": 1, "Bug": 2, "Rock": 1, "Ghost": 1, "Dragon": 1, "Dark": 1, "Steel": 0.5, "Fairy": 1, "None": 0},
    "Ghost": {"Normal": 0, "Fire": 1, "Water": 1, "Grass": 1, "Electric": 1, "Ice": 1, "Fighting": 1, "Poison": 1, "Ground": 1, "Flying": 1, "Psychic": 2, "Bug": 1, "Rock": 1, "Ghost": 2, "Dragon": 1, "Dark": 0.5, "Steel": 1, "Fairy": 1, "None": 0},
    "Dragon": {"Normal": 1, "Fire": 1, "Water": 1, "Grass": 1, "Electric": 1, "Ice": 1, "Fighting": 1, "Poison": 1, "Ground": 1, "Flying": 1, "Psychic": 1, "Bug": 1, "Rock": 1, "Ghost": 1, "Dragon": 2, "Dark": 1, "Steel": 0.5, "Fairy": 0, "None": 0},
    "Dark": {"Normal": 1, "Fire": 1, "Water": 1, "Grass": 1, "Electric": 1, "Ice": 1, "Fighting": 0.5, "Poison": 1, "Ground": 1, "Flying": 1, "Psychic": 2, "Bug": 1, "Rock": 1, "Ghost": 2, "Dragon": 1, "Dark": 0.5, "Steel": 1, "Fairy": 0.5, "None": 0},
    "Steel": {"Normal": 1, "Fire": 0.5, "Water": 0.5, "Grass": 1, "Electric": 0.5, "Ice": 2, "Fighting": 1, "Poison": 1, "Ground": 1, "Flying": 1, "Psychic": 1, "Bug": 1, "Rock": 2, "Ghost": 1, "Dragon": 1, "Dark": 1, "Steel": 0.5, "Fairy": 2, "None": 0},
    "Fairy": {"Normal": 1, "Fire": 1, "Water": 1, "Grass": 1, "Electric": 1, "Ice": 1, "Fighting": 2, "Poison": 0.5, "Ground": 1, "Flying": 1, "Psychic": 1, "Bug": 1, "Rock": 1, "Ghost": 1, "Dragon": 2, "Dark": 2, "Steel": 0.5, "Fairy": 1, "None": 0},
    "None": {"Normal": 0, "Fire": 0, "Water": 0, "Grass": 0, "Electric": 0, "Ice": 0, "Fighting": 0, "Poison": 0, "Ground": 0, "Flying": 0, "Psychic": 0, "Bug": 0, "Rock": 0, "Ghost": 0, "Dragon": 0, "Dark": 0, "Steel": 0, "Fairy": 0, "None": 0},
}

# Función para calcular el factor de tipo
def type_factor(types1, types2):
    if (types1[0] not in type_chart or types1[1] not in type_chart) or (types2[0] not in type_chart or types2[1] not in type_chart):
        print("Error hay un tipo invalido....", types1, types2)
        return -1, -1
    af = 1
    df = 1
    for i in range(2):
        for j in range(2):
            af += type_chart[types1[i]][types2[j]]
            df += type_chart[types2[i]][types1[j]]
    factor1 = af / df
    factor2 = df / af

    return factor1, factor2

def normalize_tf(tp1, tp2):
    f1, f2 = type_factor(tp1, tp2)
    # return f1 / f2
    return f1 - f2

# Normaliza las columnas seleccionadas de un DataFrame en un rango definido.
def normalize_columns(df: pd.DataFrame, columns, min_val=-10.0, max_val=10.0):
    df_normalized = df.copy()  # Crear una copia del DataFrame para no modificar el original

    for col in columns:
        col_min = df[col].min()  # Valor mínimo de la columna
        col_max = df[col].max()  # Valor máximo de la columna
        
        # Normalizar la columna a [min_val, max_val]
        df_normalized[col] = ((df[col] - col_min) / (col_max - col_min)) * (max_val - min_val) + min_val

    return df_normalized

def preprocess_pokemon_data(pokemon_df):
    """
    Preprocesar los datos de Pokémon:
    - Rellenar valores NaN en 'Type 2' con 'None'.
    - Codificar 'Legendary' como binario.
    - Eliminar la columna 'Generation'.
    """
    pokemon_df["Type 2"].fillna("None", inplace=True)
    pokemon_df["Legendary"] = pokemon_df["Legendary"].astype(int)
    pokemon_df.drop(["Generation"], axis=1, inplace=True)
    return pokemon_df

def get_pokemon_types(pokemon_df, pokemon_id):
    """
    Obtener los tipos de un Pokémon dado su ID.
    """
    pokemon = pokemon_df[pokemon_df["#"] == pokemon_id]
    if pokemon.empty:
        print(f"Error: Pokémon con ID {pokemon_id} no encontrado.")
        return None, None
    return pokemon["Type 1"].values[0], pokemon["Type 2"].values[0]

def update_winner_column(battles_df):
    """
    Modificar la columna 'Winner' para asignar 1 o 0 según el ganador.
    """
    battles_df["Winner"] = battles_df.apply(lambda row: 1 if row["First_pokemon"] == row["Winner"] else 0, axis=1)