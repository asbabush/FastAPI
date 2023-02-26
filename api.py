import shutil
from typing import List
from fastapi import APIRouter, UploadFile, File, Form, Request
from schemas import UploadVideo, GetVideo, Message
from fastapi.responses import JSONResponse

video_router = APIRouter()


@video_router.post("/")
async def root(title: str = Form(...), description: str = Form(...), file: UploadFile = File(...)):
    info = UploadVideo(title=title, description=description)
    with open(f"/home/anton/PycharmProjects/FastAPI/output_file/anton_{file.filename}", "wb") as bufer:
        shutil.copyfileobj(file.file, bufer)

    return {"file_name": file.filename, "info": info}


@video_router.post("/img")
async def import_img(files: List[UploadFile] = File(...)):
    for img in files:
        with open(
                f"/home/anton/PycharmProjects/FastAPI/output_file/anton_{img.filename}",
                "wb",
        ) as bufer:
            shutil.copyfileobj(img.file, bufer)

    return {"file_name": "Good"}


@video_router.get("/video", response_model=GetVideo, responses={404: {"model": Message}})
async def get_video():
    user = {'user_id': '123456', 'user_name': 'Pipec'}
    video = {'title': 'Title', 'description': 'Description'}
    info = GetVideo(user=user, video=video)
    return JSONResponse(status_code=200, content=info.dict())


@video_router.get("/test")
async def return_test(req: Request):
    print(req.url)
    return {}
