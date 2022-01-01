# -*- coding: utf-8 -*-

from fastapi import (
    APIRouter,
    Depends
)
from sqlalchemy.orm import Session

from backend.db.models import User
from backend.db.models.database import db_session
from backend.db.repositories.user import UserRepository
from backend.schemas.user import UserSchema
from backend.schemas.default_schema import DefaultSchema


router = APIRouter(tags=["user", ])


@router.post("/user/", tags=["user", ], response_model=DefaultSchema)
async def create_user(request: UserSchema, db_session: Session = Depends(db_session)):
    user_dict = dict(request)
    user = User()

    with UserRepository(db_session) as user_repository:
        user.name = user_dict["name"]
        user.login = user_dict["login"]
        user.email = user_dict["email"]
        user.password = user.encrypt_password(user_dict["password"])

        user_repository.add(user)

    return {
        "success": True,
        "reason": f"User {user.name} created sucessfully"
    }

