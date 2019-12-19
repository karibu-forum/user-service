from user_service.db.repository.exceptions import NotFoundError, UpdateError


def validate_write_fields(raw_data, writable_fields, exception_cls=UpdateError):
    write_fields = {}
    for name, value in raw_data.items():
        if name in writable_fields:
            write_fields[name] = value
        else:
            raise exception_cls('Cannot write this field {}'.format(name))
    return write_fields


def set_write_fields(instance, write_data):
    for key, val in write_data.items():
        setattr(instance, key, val)
