from sqlalchemy import *
# from sqlalchemy.ext.declarative import declarative_base
# Base = declarative_base()
from main_project.model.base import Base
from sqlalchemy.orm import relationship
from connector import cnx
from sqlalchemy.schema import UniqueConstraint

class Person(Base):
    __tablename__ = "person_details"
    __table_args__ = {'extend_existing': True}
    first_name = Column(String(50))
    dob = Column('dob',Date())
    last_name = Column('last_name',String(50))
    phone_number = Column('phone_number',Numeric)
    email = Column('email',String(50),unique = True)
    id = Column('id',Integer,primary_key=True)
    stud = relationship("Student",backref = "personal_details.id")
    add = relationship("address",backref = "personal_details.id")

"""
Student table is given below
"""

class Student(Base):
    __tablename__ = "student"
    __table_args__ = {'extend_existing': True}
    person_id = Column('person_id',Integer,ForeignKey('person_details.id'),nullable =False)
    id = Column('id', Integer,primary_key = True)
    roll_number = Column("roll_number",Integer)
    batch = Column("batch",Integer)
    level = Column("student_level",Integer)
    enroll_stud_fk = relationship("Enrollments", backref="student.id")

"""
Teacher/professor table is created below
"""


class teacher(Base):
    __tablename__ = "teacher"
    __table_args__ = {'extend_existing': True}

    emp_id = Column('emp_id', Integer, primary_key=True)
    salary = Column('salary',Integer)
    person_id = Column('person_id', Integer,ForeignKey('person_details.id'))
    doj = Column('date_of_joining', Date())
    enroll_course_teacher_id_ref = relationship("Course", backref="teacher.emp_id")



"""
address table is given below
"""

class address(Base):

    __tablename__ = "address"
    __table_args__ = {'extend_existing': True}
    person_id = Column('person_id',Integer,ForeignKey('person_details.id'))
    address_id = Column('address_id',Integer,primary_key = True)
    street = Column('street',String(500))
    city = Column('city',String(500))
    country = Column('country',String(500))
    postal_code = Column('postal_code',Integer)


Base.metadata.create_all(cnx)