from celery import Celery
from celery.signals import task_postrun

include_modules = [
    'user_service.api.rest.user',
]

celery_config = dict(
    task_default_queue='default',
    task_ignore_result=True,
    worker_hijack_root_logger=False,
    worker_redirect_stdouts_level='INFO',
    task_soft_time_limit=60,
    task_always_eager=False,
    task_eager_propagates=False
)


celery = Celery(
    'celery',
    broker='redis://redis:6379/0',
    include=include_modules
)

celery.conf.update(**celery_config)
@task_postrun.connect
def task_postrun_handler(sender=None, headers=None, body=None, **kwargs):
    from user_service.db.session import get_session

    # Clear DB session between tasks
    session = get_session()
    session.remove()
