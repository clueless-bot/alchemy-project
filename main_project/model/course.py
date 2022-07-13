from sqlalchemy import *
from base import Base

class course(Base):
    __tablename__ = 'course'

    course_id = Column("course_id",Integer,primary_key = True)
    id = Column("id",Integer,ForeignKey('person.id'))
    title = Column('title',String(100))
    credits = Column('credits',String(100))
    level = Column('level',String(100))
    total = Column('total',Integer)
class exam(Base):
    __tablename__ = 'exam'

    exam_number = Column("exam_number",Integer, primary_key =True)
    id = Column('id',Integer,ForeignKey('person.id'))
    exam_date = Column("exam_date",Date())
    supervisor = Column("supervisor",String(100))
    total_marks = Column("total_marks",Integer)