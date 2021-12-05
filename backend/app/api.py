# -*- coding: utf-8 -*-

##############################################################################
# @Author: Ildomar Carvalho
# @Email:  ildomar.carvalho@accenture.com
# @Date:   2021-12-04 11:12:42
##############################################################################

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = [
    "http://localhost:3000",
    "localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


users = [
    {
        "id": 1,
        "login": "admin",
    },
    {
        "id": 2,
        "login": "ildomar",
    },
]

@app.get('/', tags=["root", ])
async def root() -> dict:
    return {
        "success": True,
        "message": "First Version",
    }

@app.get('/users', tags=["users", ])
async def get_users() -> dict:
    return {
        "success": True,
        "users": users,
    }

@app.post("/user", tags=["users", ])
def add_user(user: dict) -> dict:
    users.append(user)
    print("USER: ", user)

    return {
        "success": True,
    }

@app.put("/user/{id}", tags=["users", ])
async def update_user(id: int, body: dict) -> dict:
    for user in users:
        if user["id"] == id:
            user["login"] = body["login"]

    return {
        "success": True,
    }

@app.delete("/user/{id}", tags=["users", ])
async def delete_user(id: int) -> dict:
    for user in users:
        if user["id"] == id:
            users.remove(user)

    return {
        "success": True,
    }

