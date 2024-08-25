from datetime import datetime
from pydantic import BaseModel, Field

class UserRequest(BaseModel):
    username: str
    email: str
    password: str
    date: datetime | None = None


class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    date: datetime
    class Config:
        from_attributes = True

