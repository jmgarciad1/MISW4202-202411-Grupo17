from flask import request
from flask_restful import Resource

from micro1.resources.relational_bd import RelationalBdResource


class NotificacioService(Resource):


    resource: RelationalBdResource = RelationalBdResource()
    def create_notification(self):
        response: dict= {
                "statusValid":True,
                "mensaje":{
                    "id":self.resource.get_id(),
                    "mensaje":request.json["mensajeNotificacion"],
                    "telemtria": {
                        "tipoNotificacion":request.json["tipoNotificacion"]
                    },
                    "usuario": request.json["usuario"]
                },
                "errores": [],
                "mensajeTranpa": False
            }
        try:
            response["mensaje"]["id"] = self.resource.get_id()
            response["mensaje"]["mensaje"] = request.json["mensajeNotificacion"]
            response["mensaje"]["telemtria"]["tipoNotificacion"] = request.json["tipoNotificacion"]
            response["mensaje"]["usuario"] = request.json["usuario"]


        except Exception as e:
             response["errores"] =[]
             response["errores"].append(str(e))
        

        return response