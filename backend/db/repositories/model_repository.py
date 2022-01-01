# -*- coding: utf-8 -*-

from sqlalchemy.exc import IntegrityError
from sqlalchemy.sql.expression import false

from backend.exceptions.exceptions import CustomException


class ModelRepository():
    def __init__(self, db_session, model):
        self.db_session = db_session
        self.model = model

    def __enter__(self):
        return self

    def __exit__(self, exc_type, value, traceback):
        if exc_type is None:
            self.commit()
        else:
            self.rollback()

    def commit(self):
        try:
            self.db_session.commit()
        except IntegrityError as exc:
            self.rollback()
            raise CustomException(exc)

    def add(self, obj):
        self.db_session.add(obj)

    def rollback(self):
        self.db_session.rollback()

    def create_query(self, **kwargs):
        pk = kwargs.get("pk", None)
        created_after = kwargs.get("created_after", None)
        updated_after = kwargs.get("updated_after", None)
        created_before = kwargs.get("created_before", None)
        updated_before = kwargs.get("updated_before", None)
        with_deleted = kwargs.get("with_deleted", False)
        order_by = kwargs.get("order_by")

        query = self.db_session.query(self.model)
        if pk:
            query = query.filter(self.model.pk == pk)
        if created_after:
            query = query.filter(self.model.created_on >= created_after)
        if updated_after:
            query = query.filter(self.model.updated_on >= created_after)
        if created_before:
            query = query.filter(self.model.created_on <= created_before)
        if updated_before:
            query = query.filter(self.model.updated_on <= updated_before)
        if with_deleted:
            query = query.filter(self.model.deleted == false())
        if order_by:
            query = query.order_by(order_by)

        return query

    def one_or_none(self, **kwargs):
        return self.create_query(**kwargs).one_or_none()

