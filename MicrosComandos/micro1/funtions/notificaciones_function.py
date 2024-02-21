from flask import request
from flask_restful import Resource

from micro1.services.notificaciones_service import NotificacioService


class NotificacionFunction(Resource):



    service = NotificacioService()


    def post(self):
        return self.service.create_notification()
 