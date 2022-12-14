from ast import For
from typing import List
from uuid import UUID, uuid4
from fastapi import FastAPI, HTTPException, Request
import hashlib

from model import Gender, Role, User, UserUpdateRequest

app = FastAPI()

db: List[User] = [
  User(
    id=UUID("d929fdfb-ad76-4ac3-88bc-11a65d1f6fc7"), 
    first_name="Jamal", 
    last_name="Ahmed",
    gender=Gender.male,
    roles=[Role.admin, Role.user]
  ),
  User(
    id=UUID("d98e5a31-dca5-4c6a-ae95-344cce643c0f"), 
    first_name="Alex", 
    last_name="Jones",
    gender=Gender.male,
    roles=[Role.student]
  ),
  User(
    id=uuid4(), 
    first_name="Random", 
    last_name="Users",
    gender=Gender.male,
    roles=[Role.student]
  ),
]

@app.get("/")
async def root():
  return {"Hello": "Fyan"}

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
    if user.id == user_id:
      db.remove(user)
      return True
  raise HTTPException(
    status_code=404,
    detail=f"User with id: {user_id} does not exists"
  )

@app.put("/api/v1/users/{user_id}")
async def update_user(user_update: UserUpdateRequest, user_id: UUID):
  for user in db:
    if user.id == user_id:
      if user_update.first_name is not None:
        user.first_name = user_update.first_name
      if user_update.last_name is not None:
        user.last_name = user_update.last_name
      if user_update.middle_name is not None:
        user.middle_name = user_update.middle_name
      if user_update.roles is not None:
        user.roles = user_update.roles
      return True
  raise HTTPException(
    status_code=404,
    detail=f"User with id: {user_id} does not exists"
  )

@app.post("/api/v1/validhook")
async def validhook(request: Request):
  simulatorSecretKey = "6g48jk8Sc307tchciRxzkZ"
  headSignature = request.headers.get("Signature")
  message_body = await request.body()
  message_string = str(message_body)
  splitSignature = headSignature.split(";")
  signature = splitSignature[0]
  timestamps = splitSignature[1]
  hash_obj = hashlib.md5(simulatorSecretKey.encode('utf-8') + signature.encode('utf-8') + timestamps.encode('utf-8'))

  return {
    "status":"ok", 
    "validateSignature": hash_obj.hexdigest()
  }