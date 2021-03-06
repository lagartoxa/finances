# -*- coding: utf-8 -*-

from pydantic import BaseModel


class UserSchema(BaseModel):
    name: str
    email: str
    login: str
    password: str

