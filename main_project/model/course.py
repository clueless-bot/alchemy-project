from sqlalchemy import Column,String,Integer,Date,ForeignKey,Float
from main_project.model.base import Base,cnx
from sqlalchemy.orm import relationship
from main_project.model.person import teacher

class Course(Base):
    __tablename__ = 'course'
    __table_args__ = {'extend_existing': True}
    course_id = Column("course_id", Integer, primary_key=True)
    teacher_id = Column("emp_id", Integer, ForeignKey(teacher.emp_id))
    title = Column('title', String(100))
    credits = Column('credits', Float)
    level = Column('level', Integer)
    total = Column('total', Integer)
    enroll_course_fk = relationship("Enrollments", backref="course.course_id")


class Exam(Base):
    __tablename__ = 'exam'
    __table_args__ = {'extend_existing': True}
    exam_number = Column("exam_number", Integer, primary_key=True)
    exam_date = Column("exam_date", Date())
    supervisor = Column("supervisor", String(100))
    total_marks = Column("total_marks", Integer)
    enroll_attempt_exam_number_fk = relationship("Attempt", backref="exam.exam_number")

Base.metadata.create_all(cnx)