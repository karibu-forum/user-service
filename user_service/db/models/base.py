from sqlalchemy import Column, DateTime
import datetime


def utcnow():
    return datetime.datetime.utcnow()

class BaseModelMixin:
    created_at = Column(DateTime, default=utcnow)
    updated_at = Column(DateTime, default=utcnow, onupdate=utcnow)

    @classmethod
    def get_writable_columns(cls, exclude_primary_key=True, exclude_created_updated_at=True):
        columns = []
        for col in cls.__table__.columns:
            if exclude_primary_key and col.primary_key:
                continue
            if exclude_created_updated_at and col.name in ('created_at', 'updated_at'):
                continue

            columns.append(col)

        return columns

    @classmethod
    def get_writable_column_names(cls):
        return [col.name for col in cls.get_writable_columns()]
