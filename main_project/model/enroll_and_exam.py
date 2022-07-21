from main_project.model.base import *
from sqlalchemy.orm import *
from sqlalchemy import *


class Enrollments(Base):
    __tablename__ = 'enrollment'
    __table_args__ = {'extend_existing': True}

    enroll_id = Column("enrollment_id", Integer, primary_key=True)
    course_id = Column('enroll_course_id',Integer,ForeignKey('course.course_id'))
    student_id = Column('student_id',Integer,ForeignKey('student.id'))
    student = relationship('Student')
Base.metadata.create_all(cnx)

