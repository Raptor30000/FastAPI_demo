from typing import List
from uuid import UUID, uuid4
from pydantic import BaseModel
from enum import Enum


class Gender(str, Enum):
    male = "male"
    female = "female"


class Role(str, Enum):
    admin = "admin"
    user = "user"
    student = "student"


class User(BaseModel):
    id: UUID | None = uuid4()
    first_name: str
    last_name: str
    middle_name: str | None = None
    gender: Gender
    role: List[Role]
