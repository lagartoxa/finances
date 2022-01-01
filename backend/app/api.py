# -*- coding: utf-8 -*-

from fastapi import (
    Depends,
    FastAPI
)
from fastapi.middleware.cors import CORSMiddleware

from sqlalchemy.orm import Session

from backend.authentication.token import get_current_user
from backend.routers import user
from backend.schemas.user import UserSchema


app = FastAPI()
app.include_router(user.router)

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
async def root(current_user: UserSchema = Depends(get_current_user)) -> dict:
    return {
        "success": True,
        "message": "First Version",
    }

