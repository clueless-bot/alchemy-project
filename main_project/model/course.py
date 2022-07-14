from sqlalchemy import *
#from base import Base
from connector import cnx
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
from main_project.model.person import *

class Course(Base):
    __tablename__ = 'course'
    #__table_args__ = {'extend_existing': True}

    # def __int__(self,course_id,person_id,title,credits,level,total):
    #     self.course_id = course_id
    #     self.person_id = person_id
    #     self.title = title
    #     self.credits = credits
    #     self.level = level
    #     self.total = total


    course_id = Column("course_id", Integer, primary_key=True)
    person_id = Column("id", Integer, ForeignKey('person_details.id'))
    title = Column('title', String(100))
    credits = Column('credits', Float)
    level = Column('level', Integer)
    total = Column('total', Integer)

    #def add_column(engine, table_name, column):
        #column_name = column.compile(dialect=engine.dialect)
        #column_type = column.type.compile(engine.dialect)
        #engine.execute('ALTER TABLE %s ADD COLUMN %s %s' % (table_name, column_name, column_type))
        #engine.execute('ALTER TABLE course Modify column credits Float; ')
        #engine.execute('ALTER TABLE course Modify column level Integer; ')

    #add_column(cnx, __tablename__, level)


class Exam(Base):
    __tablename__ = 'exam'
    #__table_args__ = {'extend_existing': True}

    exam_number = Column("exam_number", Integer, primary_key=True)
    person_id = Column(Integer, ForeignKey('person_details.id'))
    exam_date = Column("exam_date", Date())
    supervisor = Column("supervisor", String(100))
    total_marks = Column("total_marks", Integer)


Base.metadata.create_all(cnx)
