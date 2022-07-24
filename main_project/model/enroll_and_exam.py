from main_project.model.base import Base,cnx
from sqlalchemy.orm import relationship
from sqlalchemy import Column,Integer,ForeignKey
from main_project.model.course import Course
from main_project.model.person import Student


class Enrollments(Base):
    """Enrollment Table"""
    __tablename__ = 'enrollment'
    __table_args__ = {'extend_existing': True}

    enroll_id = Column("enrollment_id", Integer, primary_key=True)
    course_id = Column('enroll_course_id',Integer,ForeignKey(Course.course_id))
    student_id = Column('student_id',Integer,ForeignKey(Student.id))
    student = relationship('Student')
Base.metadata.create_all(cnx)

