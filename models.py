from typing import Optional

import ormar
from db import database, metadata
import datetime


class MainMeta(ormar.ModelMeta):
    metadata = metadata
    database = database


class User(ormar.Model):
    class Meta(MainMeta):
        pass

    id: int = ormar.Integer(primary_key=True)
    user: str = ormar.String(max_length=100)


class Video(ormar.Model):
    class Meta(MainMeta):
        pass

    id: int = ormar.Integer(primary_key=True)
    title: str = ormar.String(max_length=100)
    description: str = ormar.String(max_length=500)
    file: str = ormar.String(max_length=1000)
    create_at: datetime.datetime = ormar.DateTime(default=datetime.datetime.now())
    user: Optional[User] = ormar.ForeignKey(User)
