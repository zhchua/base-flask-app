from sqlalchemy import ForeignKey,Column, Integer

from helpers.db import Base
from orm_classes.account import Account
from orm_classes.tag import Tag

class Accounttag(Base):

    __tablename__ = 'usertag'

    id = Column(Integer, primary_key = True)

    account_id = Column(Integer, ForeignKey(f'{Account.__tablename__}.id'), nullable = False)
    tag_id = Column(Integer, ForeignKey(f'{Tag.__tablename__}.id'))

