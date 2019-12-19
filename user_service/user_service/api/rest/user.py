from flask import Blueprint, jsonify, request
from user_service.db.session import get_session, session_commit
from user_service.app.redis import redis_conn
from user_service.api.rest.exceptions import BadRequestError, ResourceNotFoundError
from user_service.db.models.user import User

user_api = Blueprint('user', __name__)


@user_api.route('/ping', methods=['GET'])
def test():
    return 'pong', 200

@user_api.route('/users/create', methods=['POST'])
def user_create():
    data = request.json
    email = data['email']
    password = data['password']
    username = data['username']


@user_api.route('/users/<string:user_id>', methods=['GET'])
def user_get(user_id):
    pass

@user_api.route('/users/<string:user_id>', methods=['PATCH'])
def user_update(user_id):
    pass
