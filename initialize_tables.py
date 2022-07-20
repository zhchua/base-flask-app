'''
This script initializes tables into the DB according to IMPORTED defined classes
'''

from helpers.db import engine, Base
from orm_classes.account import Account
from orm_classes.tag import Tag
from orm_classes.accounttag import Accounttag
from orm_classes.contact import ContactInfo

Base.metadata.create_all(engine)