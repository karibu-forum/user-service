from user_service.lib.exceptions import BaseException


class APIException(BaseException):
    status_code = 400


class BadRequestError(APIException):
    status_code = 400


class UnauthorizedError(APIException):
    status_code = 401


class ResourceNotFoundError(APIException):
    status_code = 404
