from sqlalchemy import Column, Integer, String, Text

from helpers.db import Base

class Tag(Base):
    __tablename__ = 'tag'

    id = Column(Integer, primary_key = True)

    name = Column(String(256))
    description = Column(Text)