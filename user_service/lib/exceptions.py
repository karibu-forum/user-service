class BaseException(Exception):

    def __init__(self, message=None, data=None, code=None):
        super().__init__(message)
        self.message = message
        self.data = data
        self.code = code

class FieldError:
    def __init__(self, field, message=None, code=None):
        self.field = field
        self.message = message
        self.code = code


class FieldErrorsMixin:
    """
    Mixin to add field_errors property to an exception class
    """
    def __init__(self, *args, field_errors=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.field_errors = field_errors or []


class FieldErrorsException(FieldErrorsMixin, BaseException):
    pass