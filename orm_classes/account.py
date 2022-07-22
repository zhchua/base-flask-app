from sqlalchemy import Boolean, DateTime, Column, Integer, String, func, Text

from helpers.db import Base

class Account(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key = True)
    username = Column(String(256), unique = True)
    pwtext = Column(Text)

    createts = Column(DateTime, server_default=func.now())
    createby = Column(Integer)
    modts = Column(DateTime, onupdate = func.now())
    modby = Column(Integer)

    deleted = Column(Boolean, default=False)

    def __init__(self, username : str, pwhash : str):
        self.username = username
        self.pwhash = pwhash