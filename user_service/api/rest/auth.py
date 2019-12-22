from flask import Blueprint, jsonify, request
from user_service.db.session import get_session, session_commit
from user_service.app.redis import redis_conn
from user_service.api.rest.exceptions import BadRequestError, ResourceNotFoundError
from user_service.db.models import User
from user_service.lib.celery import task


auth_api = Blueprint('auth', __name__)


@auth_api.route('/login', methods=['POST'])
def login():
    pass

@auth_api.route('/session/logout', methods=['POST'])
def logout():
    pass
