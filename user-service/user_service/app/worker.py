from user_service.app.celery import app   # noqa, this module needs "app"
from user_service.app.initialization import initialize

initialize()
