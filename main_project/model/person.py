from sqlalchemy import *
from main_project.model.base import Base
from sqlalchemy.orm import relationship
from connector import cnx
from sqlalchemy.schema import UniqueConstraint
#from main_project.controller.enrollment import *

#from sqlalchemy.ext.declarative import declarative_base
#Base = declarative_base()

class Person(Base):
    __tablename__ = "person_details"
    __table_args__ = {'extend_existing': True}

    first_name = Column(String(50))



    """Adding Columns"""
    # def add_column(engine, table_name, column):
    #     column_name = column.compile(dialect=engine.dialect)
    #     column_type = column.type.compile(engine.dialect)
    #     #engine.execute('ALTER TABLE %s ADD COLUMN %s %s' % (table_name, column_name, column_type))
    #     engine.execute('UPDATE person SET phone_number Numeric;')


    dob = Column('dob',Date())
    last_name = Column('last_name',String(50))
    phone_number = Column('phone_number',Numeric)
    email = Column('email',String(50),unique = True)
    id = Column('id',Integer,primary_key=True)
    # add_column(cnx, __tablename__, id)

    """Adding primary key"""

    # def add_column(engine, table_name,column):
    #     column_name = column.compile(dialect=engine.dialect)
    #     column_type = column.type.compile(engine.dialect)
    #     #engine.execute('ALTER TABLE %s ADD COLUMN %s %s' % (table_name, column_name, column_type))
    #     #engine.execute('ALTER TABLE %s AUTO_INCREMENT=1' % (table_name))

    # id = Column('id',Integer)
    #add_column(cnx,__tablename__,id)
    #course_fk = relationship("Course", backref="person_details.id")
    #exam_fk = relationship("Exam",backref="person_details.id")
    #enroll_course_fk = relationship("Enrollment",backref = "personal_details.id")

    # Cs = relationship("C", backref="A.id")
    #__table_args__ = (UniqueConstraint('email') ,)
#https://www.youtube.com/watch?v=T6Q6bsv05To&list=PL4iRawDSyRvVd1V7A45YtAGzDk6ljVPm1&index=8



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



    # def add_col(engine, table_name, column):
    #     column_name = column.compile(dialect=engine.dialect)
    #     column_type = column.type.compile(engine.dialect)
        # engine.execute('ALTER TABLE %s ADD COLUMN %s %s' % (table_name, column_name, column_type))
        # engine.execute('ALTER TABLE course Modify column credits Integer; ')
        # engine.execute('UPDATE student SET level=''')
    #     engine.execute("alter table %s rename column level to student_level" % (table_name))
    # add_col(cnx,__tablename__,level)
"""add_column(cnx, __tablename__,credits)
Teacher/professor table is created below
"""


class teacher(Base):
    __tablename__ = "teacher"
    __table_args__ = {'extend_existing': True}

    emp_id = Column('emp_id', Integer, primary_key=True)
    salary = Column('salary',Integer)
    person_id = Column('person_id', Integer,ForeignKey('person_details.id'))
    doj = Column('date_of_joining', Date())

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