import shutil
from typing import List
from fastapi import FastAPI, UploadFile, File

app = FastAPI()


@app.post("/")
async def root(file: UploadFile = File(...)):
    with open(f"anton_{file.filename}", "wb") as bufer:
        shutil.copyfileobj(file.file, bufer)

    return {"file_name": file.filename}


@app.post("/img")
async def import_img(files: list[UploadFile] = File(...)):
    for img in files:
        with open(
            f"/home/anton/PycharmProjects/FastAPI/output_file/anton_{img.filename}",
            "wb",
        ) as bufer:
            shutil.copyfileobj(img.file, bufer)

    return {"file_name": "Good"}
