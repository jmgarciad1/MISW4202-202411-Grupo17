import asyncio
import aiohttp
import csv
from datetime import datetime

urls = [
    "http://127.0.0.1:5001/notificacion1",
    "http://127.0.0.1:5002/notificacion2",
    "http://127.0.0.1:5003/notificacion3",
]
users = 5

async def post_data(url):
    async with aiohttp.ClientSession() as session:
        data = {
             "usuario": 1,
             "tipoNotificacion": 1,
             "mensajeNotificacion": "mensaje",
             "fechaNotificaicon": "20204-01-01 12:05:05"
        }
        async with session.post(url, json=data) as response:
            data = await response.json()
            return data

async def main():
    responses = []

    tasks = [post_data(url) for url in urls]
    responses = await asyncio.gather(*tasks)

    if all(response == responses[0] for response in responses):
        print("Todas las respuestas son iguales. Eligiendo la primera:", responses[0])
        respuesta = "Todas las respuestas son iguales. Eligiendo la primera: " + str(responses[0])
    else:
        for response in responses:
            if responses.count(response) > 1:
                print("Respuesta repetida:", response)
                respuesta = "Se encontro inconsistencia y se toma: " + str(response)
                break

    with open("data.csv", "a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Fecha", "Respuesta", "respuesta elegida"])
        for response in responses:
            writer.writerow([datetime.now().isoformat(), response, respuesta])

n = 5  # Number of times to run the code block

for _ in range(users):
    asyncio.run(main())