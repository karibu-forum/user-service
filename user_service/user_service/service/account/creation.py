from user_service.service.authentication.password import (
    check_password_strength_default, hash_password
)
from user_service.utils.dates import utcnow

def create_user_account(email, password, username):
    args = {}
    try:
        check_password_strength_default(password)
    except PasswordStrengthError as e:
        pass
        # raise CreateUserError(e.message)
    hashed_password = hash_password(password)
    args['password_updated_at'] = utcnow()
    args.update(
        email=email, hashed_password=hashed_password, username=username
    )

