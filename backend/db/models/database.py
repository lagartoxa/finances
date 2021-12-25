# -*- coding: utf-8 -*-

from sqlalchemy import (
    BigInteger,
    Column,
    create_engine,
    func,
    DateTime,
    Integer
)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import sessionmaker

import time


SQLALCHEMY_DATABASE_URL = "postgresql://project:project@localhost/finances"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


class BaseTable(Base):
    __abstract__ = True

    pk = Column(BigInteger, primary_key=True, index=True)
    rm_timestamp = Column(Integer, nullable=False, server_default='0')
    created_on = Column(DateTime, nullable=False, server_default=func.now())
    updated_on = Column(
        DateTime, nullable=False,
        server_default=func.now(), onupdate=func.now()
    )

    @hybrid_property
    def deleted(self):
        return self.rm_timestamp != 0

    @deleted.setter
    def deleted(self, value):
        self.rm_timestamp = int(time.time() * 1000) if value else 0

    @deleted.expression
    def deleted(cls):
        return cls.rm_timestamp != 0

    @deleted.comparator
    def deleted(cls):
        return BaseTableDeletedComparator(cls.rm_timestamp)

