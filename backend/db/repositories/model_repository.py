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
        created_before = kwargs.get("created_before", None)
        updated_before = kwargs.get("updated_before", None)
        created_before = kwargs.get("created_after", None)
        updated_before = kwargs.get("updated_after", None)
        with_deleted = kwargs.get("with_deleted", False)
        order_by = kwargs.get("order_by")

        query = self.db_session.query(self.model)
        if pk:
            query.filter(self.model.pk == pk)
        if created_before:
            query.filter(self.model.created_on <= created_before)
        if updated_before:
            query.filter(self.model.updated_on <= updated_before)
        if created_after:
            query.filter(self.model.created_on >= created_after)
        if updated_after:
            query.filter(self.model.updated_on >= created_after)
        if with_deleted:
            query.filter(self.model.deleted == false())
        if order_by:
            query.order_by(order_by)

        return query

