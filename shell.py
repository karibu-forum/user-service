#!/usr/bin/env python

from user_service import app
from user_service.app import config  # noqa
from user_service.db.session import get_session
from user_service.db.models import *  # noqa
from user_service.db.repository.user import *  # noqa
from user_service.utils.dates import utcnow   # noqa

app.initialize()

session = get_session()
