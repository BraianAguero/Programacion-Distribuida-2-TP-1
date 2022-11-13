from fastapi import FastAPI,Request
from starlette.responses import RedirectResponse
import uvicorn
import client as cliente
import logging

logging.basicConfig(format='%(asctime)s %(message)s')
logging.warning('is when this event was logged.')
app=FastAPI()

@app.get("/")
def raiz():
    return RedirectResponse(url="/docs/")

@app.get("/Localizacion/{Continente}/{zone}")
def request_timzone(Continente:str,zone:str):
    geo=cliente.run(Continente,zone)
    return{
        "Hora":geo.time,
        "Zona":geo.time_zone,
        "Unix_Epoch_time":geo.epoch_time,
        }