import os
from flask import Flask
from contextlib import ContextDecorator

from user_service.db.base import initialize_database
from user_service.app import celery
from user_service.app.redis import redis_conn
from user_service.app.logging import setup_logging
import logging

_app_initialized = False


def initialize(force=False):
    """
    Configure stuff on app startup
    """
    global _app_initialized
    if _app_initialized and not force:
        return

    initialize_database()
    setup_logging()


    _app_initialized = True


def is_initialized():
    return _app_initialized


class app_context(ContextDecorator):
    """
    Use this a decorator or context manager
    """

    def __enter__(self):
        initialize()
        return self

    def __exit__(self, *exc):
        pass
