# -*- coding: utf-8 -*-

from sqlalchemy import (
    Column,
    String,
    UniqueConstraint
)

from .database import BaseTable


class User(BaseTable):
    __tablename__ = "project_user"
    # Renaming this table just to avoid having to
    # use "public.user" on psql

    name = Column(String, nullable=False, index=True)
    login = Column(String, nullable=False, index=True)
    email = Column(String, nullable=False, index=True)
    password = Column(String, nullable=False, index=True)

    __table_args__ = (
        UniqueConstraint(
            login, "rm_timestamp",
            name="project_user_login_rm_timestamp_un"
        ),
        UniqueConstraint(
            email, "rm_timestamp",
            name="project_user_email_rm_timestamp_un"
        ),
    )

