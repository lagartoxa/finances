# -*- coding: utf-8 -*-

from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import false

from backend.db.models import User
from .model_repository import ModelRepository


class UserRepository(ModelRepository):
    def __init__(self, db_session):
        ModelRepository.__init__(self, db_session, User)

