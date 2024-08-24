from dataclasses import Field
from datetime import datetime

from pydantic import BaseModel

class UserRequest(BaseModel):
    username: str
    email: str
    password: str
    datetime: datetime = Field(default_factory=datetime.now)


class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    datetime: datetime

