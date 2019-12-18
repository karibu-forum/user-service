from flask import Blueprint, jsonify, request
from user_service.db.session import get_session, session_commit
from user_service.app.redis import redis_conn
from user_service.api.rest.exceptions import BadRequestError, ResourceNotFoundError
from user_service.db.models.user import User
from user_service.lib.celery import task

@task
def test_celery_db(email):
    user = User(email=email, password = '1234')
    with session_commit() as session:
        session.add(user)


    
@task
def test_celery_add():
    print('klkmlkmlk')
    print(124+12343)

user_blueprint = Blueprint('users', __name__)


@user_blueprint.route('/ping', methods=['GET'])
def test():
    return 'pong', 200


@user_blueprint.route('/save', methods=['GET'])
def db_save():
    test_celery_db.delay('1@1.com')
    return 'saved', 200

@user_blueprint.route('/add', methods=['GET'])
def add():
    test_celery_add.delay()
    return 'added', 200
