from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from connector import cnx
from main_project.model.person import *
from main_project.model.course import *
from main_project.model.base import *
from sqlalchemy.orm import *

class Enrollments(Base):
    __tablename__ = 'enrollment'
    __table_args__ = {'extend_existing': True}

    enroll_id = Column("enrollment_id", Integer, primary_key=True)
    course_id = Column('enroll_course_id',Integer,ForeignKey('course.course_id'))
    student_id = Column('student_id',Integer,ForeignKey('student.id'))
    student = relationship('Student')
Base.metadata.create_all(cnx)

#Taking input from user and enrolling student to course
inp_student_id = int(input('Enter student id:'))
inp_course_id = int(input('Enter course id:'))
sql = text('insert into enrollment (enroll_course_id,student_id) select course.course_id, student.id from student inner join course on student.student_level = course.level where not exists (select enroll_course_id,student_id from enrollment where enroll_course_id = %s and student_id= %s)  and  course.course_id = %s and student.id = %s;' % (inp_course_id,inp_student_id,inp_course_id,inp_student_id))
results = cnx.execute(sql)
