import shutil
from typing import List
from fastapi import APIRouter, UploadFile, File, Form, Request

from models import Video
from schemas import UploadVideo, GetVideo, Message
from fastapi.responses import JSONResponse
import json


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


@video_router.post("/video")
async def create_video(video: Video):
    await video.save()
    return video


@video_router.get("/video/{video_pk}", response_model=Video, responses={404: {"model": Message}})
async def get_video(video_pk: int):
    return await Video.objects.select_related('user').get(pk=video_pk)


@video_router.get("/test")
async def return_test(req: Request):
    print(req.url)
    return {}

