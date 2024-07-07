from fastapi import FastAPI
from typing import List
from models import User, Gender, Role
from uuid import uuid4

app = FastAPI()

db: List[User] = [
    User(
        id=uuid4(),
        first_name="Adam",
        last_name="Sandler",
        gender=Gender.male,
        role=[Role.student]
    ),
    User(
        id=uuid4(),
        first_name="Joanna",
        last_name="Dark",
        gender=Gender.female,
        role=[Role.admin, Role.user]
    ),
]


@app.get("/")
async def root():
    return {'message': 'Hello There!!'}

@app.get("/api/v1/users")
async def fetch_users():
    return db

@app.post("/api/v1/users")
async def register_user(user: User):
    db.append(user)
    return {"id": user.id}
