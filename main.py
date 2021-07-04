
from fastapi import FastAPI, File, UploadFile
from minio import Minio
from file_uploader import upload
from file_download import download
from file_remove import remove
import shutil


app = FastAPI()
client = Minio("play.min.io")

db = []



@app.get('/items')
def read_items():
      return db

@app.get("/items/{name}")
def read_item(name : str):
    item = download(name)
    return {"item":item}

@app.post("/items")
async def create_item(file: UploadFile = File(...)):
    # upload(file)
    with open(file.filename, "wb") as buffer:
     shutil.copyfileobj(file.file, buffer)
    upload(file)
    return {"filename": file, "success" : 'true'}

@app.delete('/items/{name}')
def remove_item(name : str):
    item = remove(name)
    return {"item":item}