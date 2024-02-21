import random
from flask import request
from flask_restful import Resource

from micro3.resources.relational_bd import RelationalBdResource


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

            response = self.generate_fail(response=response)
        except Exception as e:
             response["errores"] =[]
             response["errores"].append(str(e))
        

        return response
    

    def generate_fail(self, response:dict):

        numero = random.randint(1, 4)
        if numero == 1:

            response["mensaje"]["mensaje"] = "mensaje falso introducido "
            response["mensaje"]["telemtria"]["tipoNotificacion"] = 3
            response["mensaje"]["usuario"] =10000000
            response["mensajeTranpa"] =True


        return response