from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {'Hello': 'World'}

@app.get("/item/{item_id}")
def getItem():
    return {'item_id': item_id, 'falg': True}