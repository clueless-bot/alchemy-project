from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from connector import cnx
Base = declarative_base()
Base.metadata.create_all(cnx)
DBSession = sessionmaker(bind=cnx)
session = DBSession()