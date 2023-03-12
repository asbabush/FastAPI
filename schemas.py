from pydantic import BaseModel
from typing import List, Optional
import datetime


class User(BaseModel):
    id: int
    username: str


class UploadVideo(BaseModel):
    title: str
    description: str


class GetVideo(BaseModel):
    user: User
    video: UploadVideo


class Message(BaseModel):
    message: str


