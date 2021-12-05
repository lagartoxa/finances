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


@app.get('/', tags=["root", ])
async def root() -> dict:
    return {
        "message": "First Version",
    }

@app.get('/users', tags=["user", ])
async def get_users() -> dict:
    return {
        "users": [
            {
                "id": 1,
                "login": "admin",
            },
            {
                "id": 2,
                "login": "ildomar",
            },
        ],
    }

