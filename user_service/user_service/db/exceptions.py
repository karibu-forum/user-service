from user_service.lib.exceptions import BaseException


class DatabaseError(BaseException):
    pass


class NotFoundError(DatabaseError):
    pass


class MutationError(DatabaseError):
    pass


class UpdateError(MutationError):
    pass


class CreateError(MutationError):
    pass
