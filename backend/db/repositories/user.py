# -*- coding: utf-8 -*-

from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import false

from backend.db.models import User
from .model_repository import ModelRepository


class UserRepository(ModelRepository):
    def __init__(self, db_session):
        ModelRepository.__init__(self, db_session, User)

    def create_query(self, **kwargs):
        query = ModelRepository.create_query(self, **kwargs)

        email = kwargs.get("email", None)
        login = kwargs.get("login", None)
        name = kwargs.get("name", None)

        if email:
            query = query.filter(User.email == email)
        if login:
            query = query.filter(User.login == login)
        if name:
            query = query.filter(User.name == name)

        return query

