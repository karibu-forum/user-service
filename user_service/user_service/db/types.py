from sqlalchemy import types
from dateutil.tz import UTC


class Text(types.TypeDecorator):
    """ Ensures we do not store blank strings, only NULL """

    impl = types.Text

    def process_bind_param(self, value, dialect):
        value = value or None
        return value


class UTCDateTime(types.TypeDecorator):
    """ Datetime with timezone that always ensures UTC tz """

    impl = types.DateTime(timezone=True)

    def process_bind_param(self, value, dialect):
        if value is not None:
            return value.astimezone(UTC)
