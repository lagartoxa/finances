# -*- coding: utf-8 -*-

from pydantic import BaseModel


class DefaultSchema(BaseModel):
    success: bool
    reason: str

