from flask import Blueprint, jsonify, request
from user_service.db.session import get_session, session_commit
from user_service.app.redis import redis_conn
from user_service.api.rest.exceptions import BadRequestError, ResourceNotFoundError
from user_service.db.models import User
from user_service.db.repository.user import get_user
from user_service.service.account.creation import create_user_account
from user_service.db.repository import exceptions as db_exceptions
from user_service.db.repository.exceptions import CreateUserError
from user_service.api.rest.serializer import UserSerializer

user_api = Blueprint('user', __name__)


@user_api.route('/ping', methods=['GET'])
def test():
    return 'pong', 200

def get_user_or_raise(user_id):
    try:
        user = get_user(user_id)
    except db_exceptions.UserNotFound:
        raise ResourceNotFoundError()
    return user


@user_api.route('/users/create', methods=['POST'])
def user_create():
    data = request.json
    email = data['email']
    password = data['password']
    username = data['username']
    try:
        user = create_user_account(email, password, username)
    except CreateUserError as e:
        pass

    user_obj = UserSerializer(user).data
    response = jsonify(user_obj)
    return response


@user_api.route('/users/<string:user_id>', methods=['GET'])
def user_get(user_id):
    user = get_user_or_raise(user_id)

    user_obj = UserSerializer(user).data
    response = jsonify(user_obj)
    return response


@user_api.route('/users/<string:user_id>', methods=['PATCH'])
def user_update(user_id):
    pass
