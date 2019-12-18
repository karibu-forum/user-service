from user_service.app.celery import celery   # noqa, this module needs "app"
from user_service.app.initialization import initialize

initialize()
