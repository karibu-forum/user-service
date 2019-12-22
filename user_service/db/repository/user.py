from sqlalchemy.sql import exists

from user_service.db.session import get_session, session_commit
from user_service.db.models import User
from user_service.db.repository.exceptions import (
    CreateUserError, UpdateUserError, UpdateUserNotFoundError, UserNotFound,
)
from user_service.db.repository.utils import validate_write_fields, set_write_fields



def create_user(
    email=None, hashed_password=None, username=None, password_updated_at=None, check_existing_email=True,
    check_existing_username=True
):
    assert email and hashed_password and username
    session = get_session()

    if check_existing_email:
        verified_user_exists = session.query(
            User.query.filter(
                User.email == email,
                User.email_verified.is_(True)
            ).exists()
        ).scalar()
        if verified_user_exists:
            raise CreateUserError('Email already exists')

    if check_existing_username:
        verified_user_exists = session.query(
            User.query.filter(
                User.username == username,
                User.email_verified.is_(True)
            ).exists()
        ).scalar()
        if verified_user_exists:
            raise CreateUserError('Username already exists')

    with session_commit(exception=CreateUserError) as session:
        user = User(
            email=email,
            password=hashed_password,
            username=username,
            password_updated_at=password_updated_at,
        )
        session.add(user)

    return user
