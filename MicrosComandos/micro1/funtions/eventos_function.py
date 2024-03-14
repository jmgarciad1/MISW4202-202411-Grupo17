from flask import request
from flask_jwt_extended import jwt_required
from flask_restful import Resource

from services.eventos_service import EventoService

class EventoFunction(Resource):



    service = EventoService()

    @jwt_required()
    def post(self):
        print(request.json)
        return self.service.create_notification()
 