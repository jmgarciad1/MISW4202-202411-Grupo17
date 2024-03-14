import csv
import random
import requests
from datetime import datetime


trampa = random.randrange(2, 99, 1)
print(trampa)
for item in range(100):
    print(item)
    data = {
    "id":1,
    "usuario": "Joan"
    }
    token = requests.post('http://127.0.0.1:5002/token', json = data)


    dataMicro= {
            "tipoEvento": 2,
            "nombreEvento": "Final mundial",
            "fechaEvento": "2024-02-02",
            "estado": "activo",
            "aforo":2500,
            "trampa": "no"
    }
    if trampa == item:
        result = requests.post('http://127.0.0.1:5001/evento1', json = dataMicro, headers={'Authorization': "fake "} )
        if str(result.status_code) == str(401):

            with open("./micro1/data.csv", "a", newline="") as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow([datetime.now().isoformat(),"USUARIO NO autorizado","SI",str(1),trampa])
    else:                
        result = requests.post('http://127.0.0.1:5001/evento1', json = dataMicro, headers={'Authorization': "Bearer "+token.json()["token"]} )

    # print(result.json())
