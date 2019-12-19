from contextlib import contextmanager

from sqlalchemy.exc import SQLAlchemyError

from user_service.db.exceptions import MutationError
from user_service.db import base


def get_session():
    return base.Session


@contextmanager
def session_commit(exception=MutationError):
    session = get_session()
    try:
        yield session
        session.commit()
    except Exception as e:
        session.rollback()
        if exception:
            raise exception(str(e))
        else:
            raise


def commit_session_or_raise(session, exception=MutationError):
    try:
        session.commit()
    except SQLAlchemyError as e:
        session.rollback()
        raise exception(str(e))
