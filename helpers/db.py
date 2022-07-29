from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

from secret.mysqldb import ENGINE_STR

engine = create_engine(ENGINE_STR, echo = True)

Base = declarative_base()