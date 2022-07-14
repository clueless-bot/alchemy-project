from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from connector import cnx
Base = declarative_base()
Base.metadata.create_all(cnx)
DBSession = sessionmaker(bind=cnx)
session = DBSession()

# from .person import Person
# from .course import Course


# DBSession = scoped_session(sessionmaker())
# Base = declarative_base()
#
# def initialize_sql(engine):
#     DBSession.configure(bind=engine)
#     Base.metadata.bind = engine
#     Base.metadata.create_all(engine)