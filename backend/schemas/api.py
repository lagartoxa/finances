# -*- coding: utf-8 -*-

from pydantic import BaseModel


class APISchema(BaseModel):
    success: bool
    reason: str

