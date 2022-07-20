from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from secret.mysqldb import ENGINE_STR

engine = create_engine(ENGINE_STR, echo = True)

Base = declarative_base()