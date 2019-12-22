from user_service.lib.exceptions import BaseException


class InvalidLoginSession(BaseException):
    pass


class ExpiredSession(InvalidLoginSession):
    pass


class AuthenticationError(BaseException):
    pass


class AuthenticationNoAccountError(AuthenticationError):
    pass


class AuthenticationBadCredentialsError(AuthenticationError):
    pass


class LoginError(BaseException):
    pass


class PasswordStrengthError(BaseException):
    pass
