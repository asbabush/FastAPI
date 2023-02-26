from pydantic import BaseModel
from typing import List


class User(BaseModel):
    user_id: int
    user_name: str


class UploadVideo(BaseModel):
    title: str
    description: str


class GetVideo(BaseModel):
    user: User
    video: UploadVideo


class Message(BaseModel):
    message: str


