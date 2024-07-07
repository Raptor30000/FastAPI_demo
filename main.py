from fastapi import FastAPI, HTTPException
from typing import List
from models import User, Gender, Role, UserUpdateRequest
from uuid import uuid4, UUID

app = FastAPI()

db: List[User] = [
    User(
        id=UUID("f35b2c78-0664-4016-9119-a864e217ede3"),
        first_name="Adam",
        last_name="Sandler",
        gender=Gender.male,
        role=[Role.student]
    ),
    User(
        id=UUID("ac6f07f4-694d-4369-a845-c282f92d89cf"),
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

@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user_id == user.id:
            db.remove(user)
            return
    raise HTTPException(status_code=404, detail=f"User with id: {user_id} not found")

@app.put("/api/v1/users/{user_id}")
async def update_user(user_update: UserUpdateRequest, user_id: UUID):
    for user in db:
        user.first_name = user_update.first_name if user_update.first_name else user.first_name
        user.middle_name = user_update.middle_name if user_update.middle_name else user.middle_name
        user.last_name = user_update.last_name if user_update.last_name else user.last_name
        user.gender = user_update.gender if user_update.gender else user.gender
        user.role = user_update.role if user_update.role else user.role