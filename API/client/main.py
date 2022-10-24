from fastapi import FastAPI,Request
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
        "Hora":respuesta
    }

@app.get("/items/{item_id}")
def read_root(item_id: str, request: Request):
    client_host = request.client.host
    return {"client_host": client_host, "item_id": item_id}