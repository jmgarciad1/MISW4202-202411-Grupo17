from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_restful import Api
from services.login import VistaLogIn

app = None


def create_flask_app():
    app = Flask(__name__)

    app.config['JWT_SECRET_KEY'] = 'frase-secreta'


    app_context = app.app_context()
    app_context.push()
    add_urls(app)
    CORS(app)

    jwt = JWTManager(app)

    @jwt.user_lookup_loader
    def user_lookup_callback(_jwt_header, jwt_data):
        return jwt_data["sub"]
    
    return app


def add_urls(app):
    api = Api(app)
    api.add_resource(VistaLogIn, '/token')



if __name__ == '__main__':
    app = create_flask_app()
    port = 5002
    app.run(port=port)