from sqlalchemy import *
from base import Base
from sqlalchemy.orm import relationship

class person(Base):
    __tablename__ = "person"


    first_name = Column(String(50))



    """Adding Columns"""
    # def add_column(engine, table_name, column):
    #     column_name = column.compile(dialect=engine.dialect)
    #     column_type = column.type.compile(engine.dialect)
    #     engine.execute('ALTER TABLE %s ADD COLUMN %s %s' % (table_name, column_name, column_type))
    #
    dob = Column('dob',Date())
    last_name = Column('last_name',String(50))

    phone_number = Column('phone_number',Integer)
    email = Column('email',String(50))
    id = Column('id',Integer,primary_key=True)
    # add_column(cnx, __tablename__, id)

    """Adding primary key"""

    # def add_column(engine, table_name, column):
    #     column_name = column.compile(dialect=engine.dialect)
        #column_type = column.type.compile(engine.dialect)
        #engine.execute('ALTER TABLE %s ADD COLUMN %s %s' % (table_name, column_name, column_type))
        #engine.execute('ALTER TABLE %s AUTO_INCREMENT=1' % (table_name))

    # id = Column('id',Integer)
    # add_column(cnx,__tablename__,id)
    Bs = relationship("course", backref="person.id")
    Cs = relationship("exam",backref = "person.id")

    # Cs = relationship("C", backref="A.id")



"""
Student table is given below
"""

class student(Base):
    __tablename__ = "student"
    person_id = Column('person_id',Integer,ForeignKey('person.id'))
    id = Column('id', Integer,primary_key = True)
    roll_number = Column("roll_number",Integer)
    batch = Column("batch",Integer)

"""
Teacher/professor table is created below
"""


class teacher(Base):
    __tablename__ = "teacher"

    emp_id = Column('emp_id', Integer, primary_key=True)
    salary = Column('salary',Integer)
    person_id = Column('person_id',    #
Integer,ForeignKey('person.id'))
    doj = Column('date_of_joining', Date())

"""
address table is given below
"""

class address(Base):
    __tablename__ = "address"
    person_id = Column('person_id',Integer,ForeignKey('person.id'))
    address_id = Column('address_id',Integer,primary_key = True)
    street = Column('street',String(500))
    city = Column('city',String(500))
    country = Column('country',String(500))
    postal_code = Column('postal_code',Integer)

