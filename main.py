# from typing import Union

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pymongo import MongoClient

app = FastAPI()
# app.mount("/static", StaticFiles(directory="static"), name="static")
# templates = Jinja2Templates(directory="templates")

# conn=MongoClient("mongodb+srv://arbeena:OCUdW6ZTnHl3f0OV@mongoyoutube.k6aeqpl.mongodb.net/notes")

# @app.get("/")
# def read_root():
#     return {"Hello": "World"}

# @app.get("/", response_class=HTMLResponse)
# async def read_item(request: Request):
#     docs=conn.notes.notes.find({})
#     newDocs=[]
#     for doc in docs:
#         newDocs.append({
#             "id":doc["_id"],
#             "note":doc["note"]
#         })
#     return templates.TemplateResponse(name="index.html", context={"request": request, "notes": newDocs})
    
# @app.get("/items/{item_id}")
# def read_items(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}