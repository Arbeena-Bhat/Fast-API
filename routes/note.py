from fastapi import APIRouter,Request
from models.note import Note
from config.db import conn
from schemas.note import noteEntity,notesEntity
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

note=APIRouter()
templates = Jinja2Templates(directory="templates")

@note.get("/", response_class=HTMLResponse)    #for reading notes
async def read_item(request: Request):   
    docs=conn.notes.notes.find({})
    newDocs=[]
    for doc in docs:
        newDocs.append({
    "id": str(doc["_id"]),
    "title": doc.get("title", ""),
    "content": doc.get("content", ""),
    "important": doc.get("important", False)
}
)
    return templates.TemplateResponse(name="index.html", context={"request": request, "notes": newDocs})

# @note.get("/items/{item_id}")
# def read_items(item_id: int, q: str|None= None):
#     return {"item_id": item_id, "q": q}
# @note.post("/")   #for adding notes
# def add_note(note: Note):
#     print(note)
#     inserted_note=conn.notes.notes.insert_one(dict(note))
#     return noteEntity(inserted_note)

# @note.post("/")    #for creating notes
# async def create_item(request: Request):   
#     form=await request.form()
#     formDict=dict(form)
#     formDict["important"]=True if formDict.get("important")=="on" else False
#     note=conn.notes.notes.insert_one(form)
#     return {"Success":True}

@note.post("/")  # for creating notes
async def create_item(request: Request):
    form = await request.form()
    formDict = dict(form)
    formDict["important"] = True if formDict.get("important") == "on" else False # type: ignore
    note = conn.notes.notes.insert_one(formDict)
    return {"Success": True}

    
