# -*- coding: utf-8 -*-

from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status
)
from fastapi.security import OAuth2PasswordRequestForm

from sqlalchemy.orm import Session

from backend.authentication.token import LocalAuthentication

from backend.db.models import User
from backend.db.models.database import db_session
from backend.db.repositories.user import UserRepository

from backend.schemas.user import UserSchema
from backend.schemas.api import APISchema
from backend.schemas.token import TokenAPISchema


router = APIRouter(tags=["user", ])


@router.post("/user", tags=["user", ], response_model=APISchema)
async def create_user(request: UserSchema, db_session: Session = Depends(db_session)):
    user = User()

    with UserRepository(db_session) as user_repository:
        user.name = request.name
        user.login = request.login
        user.email = request.email
        user.password = user.encrypt_password(request.password)

        user_repository.add(user)

    return {
        "success": True,
        "reason": f"User '{user.name}' created sucessfully"
    }


@router.post("/login", tags=["user", ], response_model=TokenAPISchema)
async def login(request: OAuth2PasswordRequestForm = Depends(), db_session: Session = Depends(db_session)):
    user = UserRepository(db_session).one_or_none(login=request.username)

    if not user:
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    if not user.verify_password(request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    token = LocalAuthentication().create_token({"sub": user.login})

    return {
        "success": True,
        "reason": f"User '{user.name}' logged in successfully.",
        "access_token": token,
        "token_type": "bearer",
    }

