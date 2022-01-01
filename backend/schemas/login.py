# -*- coding: utf-8 -*-

from pydantic import BaseModel


class Login(BaseModel):
    login: str
    password: str

