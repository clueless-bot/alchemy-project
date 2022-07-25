from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from connector import cnx
Base = declarative_base()
DBSession = sessionmaker(bind=cnx)
session = DBSession()