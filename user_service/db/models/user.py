import uuid
from sqlalchemy import Column, Index
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship, validates

from user_service.db.models.base import BaseModelMixin
from user_service.db.base import Base
from user_service.db.types import Text, UTCDateTime


class User(BaseModelMixin, Base):
    __tablename__ = 'user'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = Column(Text, nullable=False)
    password = Column(Text, nullable=False)

    email_verified_at = Column(UTCDateTime)
    password_updated_at = Column(UTCDateTime)

    username = Column(Text, nullable=False)
    deactivated_at = Column(UTCDateTime)
    last_login_time = Column(UTCDateTime)

    __table_args__ = (
        Index('user_email_unique', email, unique=True, postgresql_where=email_verified_at.isnot(None)),
        Index('user_username_unique', username, unique=True, postgresql_where=email_verified_at.isnot(None)),
    )

    @validates('email')
    def validate_email(self, key, email):
        if email and '@' not in email:
            raise ValueError('Not valid email')
        return email

    @property
    def is_active(self):
        return not self.deactivated_at

    @property
    def email_verified(self):
        return self.email_verified_at is not None
