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


class UserUpdateRequest(BaseModel):
    first_name: str | None = None
    last_name: str | None = None
    middle_name: str | None = None
    gender: Gender | None = None
    role: List[Role] | None = None
