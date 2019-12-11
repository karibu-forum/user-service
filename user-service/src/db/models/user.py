from sqlalchemy import Column, BigInteger

from hashing_service.db.models.base import BaseModelMixin
from hashing_service.db.base import Base
from hashing_service.db.types import Text

class User(BaseModelMixin, Base):
    __tablename__ = 'hashed_result'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    original_string = Column(Text, unique=True)  #  uniqueness automatically adds indexing 
    hashed_result = Column(Text)
