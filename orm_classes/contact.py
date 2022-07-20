""" Adhoc contactinfo table. Should be customized when specific requirements/details are available.
"""

from sqlalchemy import Boolean, DateTime, Column, ForeignKey, Integer, String, func, Text

from helpers.db import Base
from orm_classes.account import Account

class ContactInfo(Base):
    __tablename__ = 'contactinfo'

    id = Column(Integer, primary_key = True)
    account_id = Column(Integer, ForeignKey(f'{Account.__tablename__}.id'))
    infotype = Column(String(256), nullable = False)
    infovalue = Column(Text)

    createts = Column(DateTime, server_default=func.now())
    createby = Column(Integer)
    modts = Column(DateTime, onupdate = func.now())
    modby = Column(Integer)
