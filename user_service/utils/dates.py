from datetime import datetime

from dateutil.tz import UTC


def utcnow():
    return datetime.utcnow().replace(tzinfo=UTC)


def timestamp_to_datetime(timestamp):
    return datetime.utcfromtimestamp(timestamp).replace(tzinfo=UTC)
