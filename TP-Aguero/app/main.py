from fastapi import FastAPI
from starlette.responses import RedirectResponse
import uvicorn
import client as cliente


app=FastAPI()

@app.get("/")
def raiz():
    return RedirectResponse(url="/docs/")

@app.get("/validar/{zona}")
def request_timzone(zona:str):
    respuesta=cliente.run(zona)
    return{
        "Hora":respuesta.message
    }