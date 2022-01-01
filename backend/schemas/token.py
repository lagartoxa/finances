# -*- coding: utf-8 -*-

from pydantic import BaseModel
from typing import Optional

from .api import APISchema


class TokenAPISchema(APISchema):
    access_token: str
    token_type: str


class TokenDataSchema(BaseModel):
    login: Optional[str] = None

