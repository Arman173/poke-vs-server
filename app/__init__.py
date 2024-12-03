from flask import Flask
from app.routes.home_routes import home_blueprint
from app.routes.combat_routes import combat_blueprint
from app.routes.pokemon_routes import pokemon_blueprint
# from app.routes.user_routes import user_blueprint

def create_app():
    app = Flask(__name__)
    
    # Configuración de la app
    app.config.from_object("config.Config")
    
    # Registrar blueprints
    app.register_blueprint(home_blueprint)  # Sin prefijo; será el home
    app.register_blueprint(combat_blueprint)
    app.register_blueprint(pokemon_blueprint)
    # app.register_blueprint(user_blueprint, url_prefix="/api/users")
    
    return app
