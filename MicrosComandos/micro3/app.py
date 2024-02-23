from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from micro3.funtions.notificaciones_function import NotificacionFunction



app = None


def create_flask_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///admon_reservas.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = 'frase-secreta'
    app.config['PROPAGATE_EXCEPTIONS'] = True

    app_context = app.app_context()
    app_context.push()
    add_urls(app)
    CORS(app)

    return app


def add_urls(app):
    api = Api(app)
    api.add_resource(NotificacionFunction, '/notificacion3', '/signin/<int:id_usuario>')



if __name__ == '__main__':
    app = create_flask_app()
    port = 5003
    app.run(port=port)
