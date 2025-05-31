# from typing import Union
from fastapi import FastAPI , Request # type: ignore
from fastapi.responses import HTMLResponse # type: ignore
from fastapi.staticfiles import StaticFiles # type: ignore
from fastapi.templating import Jinja2Templates # type: ignore
from pymongo import MongoClient # type: ignore

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")
conn = MongoClient("mongodb+srv://V41BH4V:lOinrI5Kv0jidq18@intial01.ciagugc.mongodb.net")
@app.get("/", response_class=HTMLResponse)
async def read_items(request : Request ):
    docs = conn.notes.notes.find({})
    new_doc = []
    for doc in docs:
        new_doc.append({
            "id": doc["_id"],
            "note": doc["note"],
        })
    return templates.TemplateResponse("index.html", {"request": request , "new_doc": new_doc})

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str|None = "Vaibhav"):
    return {"item_id": item_id, "q": q}