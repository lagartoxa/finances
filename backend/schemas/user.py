# -*- coding: utf-8 -*-

from pydantic import BaseModel


class UserBase(BaseModel):
    name: str
    email: str
    login: str


class UserCreate(BaseModel):
    password: str


class User(BaseModel):
    pk: int

    class Config:
        orm_mode: True

