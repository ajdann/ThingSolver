from typing import Optional
from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel
from minio import Minio
from file_uploader import upload
from file_download import download
import shutil


app = FastAPI()
client = Minio("play.min.io")

db = []

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get('/items')
def read_items():
      return db

@app.get("/items/{name}")
def read_item(name : str):
    download(name)
    return {"item_id":1}

@app.post("/items")
async def create_item(file: UploadFile = File(...)):
    # upload(file)
    with open(file.filename, "wb") as buffer:
     shutil.copyfileobj(file.file, buffer)
    upload(file)
    return {"filename": file, "success" : 'true'}