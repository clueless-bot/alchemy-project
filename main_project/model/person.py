from sqlalchemy import *
from main_project.model.base import Base
from sqlalchemy.orm import relationship
from connector import cnx
from sqlalchemy.schema import UniqueConstraint

class Person(Base):
    __tablename__ = "person_details"
    __table_args__ = {'extend_existing': True}

    """Adding Columns"""
    first_name = Column(String(50))
    dob = Column('dob',Date())
    last_name = Column('last_name',String(50))
    phone_number = Column('phone_number',Numeric)
    email = Column('email',String(50),unique = True)
    id = Column('id',Integer,primary_key=True)
    Bs = relationship("Course", backref="person_details.id")
    Cs = relationship("Exam",backref="person_details.id")

"""
Student table is given below
"""

class student(Base):
    __tablename__ = "student"
    __table_args__ = {'extend_existing': True}
    person_id = Column('person_id',Integer,ForeignKey('person_details.id'),nullable =False)
    id = Column('id', Integer,primary_key = True)
    roll_number = Column("roll_number",Integer)
    batch = Column("batch",Integer)

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

