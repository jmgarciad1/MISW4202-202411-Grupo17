from datetime import datetime
from flask import request
from flask_jwt_extended import current_user
from flask_restful import Resource
import csv
from resources.relational_bd import RelationalBdResource


class EventoService(Resource):


    evento: dict = {
        "id":1,
        "tipoEvento": 2,
        "nombreEvento": "Final mundial",
        "fechaEvento": "2024-02-02",
        "estado": "activo",
        "aforo":2500
    }


    resource: RelationalBdResource = RelationalBdResource()

    def create_notification(self):
        data = request.json
        print(current_user)
        if str(current_user) == str(self.evento["id"]) :
            
            with open("data.csv", "a", newline="") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([datetime.now().isoformat(),"USUARIO AUTORIZADO",data["trampa"],str(current_user),self.evento["id"]])

            return data
        else:

            with open("data.csv", "a", newline="") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([datetime.now().isoformat(),"USUARIO NO autorizado",data["trampa"],str(current_user),self.evento["id"]])
            return "Usuario no autorizado."