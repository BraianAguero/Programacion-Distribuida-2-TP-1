from fastapi import FastAPI,Request
from starlette.responses import RedirectResponse
import uvicorn
import client as cliente


app=FastAPI()

@app.get("/")
def raiz():
    return RedirectResponse(url="/docs/")

@app.get("/validar/{Localizacion}")
def request_timzone(request:str):
    geo=cliente.run(request)
    return{
        "Hora: ":geo.time,
        "Zona: ":geo.time_zone,
        }
