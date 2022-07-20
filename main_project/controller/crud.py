from sqlalchemy import create_engine,Column,Integer,String,MetaData,Date
from sqlalchemy.orm import sessionmaker,backref,relationship,backref
from sqlalchemy.ext.declarative import declarative_base
from main_project.model.base import Base
from connector import cnx
from main_project.model.base import *
from main_project.model.course import *
from main_project.model.person import *
import itertools
"""person.py tables"""
def add_stud(obj1,obj2,obj3):
    session.add(obj1)
    session.commit()
    result = session.query(Person) \
        .with_entities(obj1.id) \
        .filter(Person.email == obj1.email).first()
    obj2.person_id = result[0]
    session.add(obj2)
    session.commit()
    obj3.person_id = result[0]
    session.add(obj3)
    session.commit()
# person1 = Person(first_name = 'suresh', dob = '2021-6-3',last_name = 'bariya',phone_number = 10981339,email = 'suresh@gmail.com')
# student1 = student(roll_number = 2468, batch = 2020,level = 12)
# address1 = address(street='prakashnagar',city='mumbai',country='india',postal_code=419203)
#
# person2 = Person(first_name = 'ayush', dob = '2020-6-3',last_name = 'shah',phone_number = 1029836456,email = 'ayush@gmail.com')
# student2 = student(roll_number = 1092, batch = 2019,level = 13)
# address2 = address(street='ayushnagar',city='delhi',country='india',postal_code=109283)
#
# person3 = Person(first_name = 'milan', dob = '2018-6-3',last_name = 'bariya',phone_number = 1296758945,email = 'milan@gmail.com')
# student3 = student(roll_number = 1154, batch = 2020,level=14)
# address3 = address(street='milanhnagar',city='mumbai',country='india',postal_code=61527)
# add_stud(person1,student1,address1)
# add_stud(person2,student2,address2)
# add_stud(person3,student3,address3)


def add_teacher(obj1,obj2,obj3):
    session.add(obj1)
    session.commit()
    result = session.query(Person) \
        .with_entities(obj1.id) \
        .filter(Person.email == obj1.email).first()
    obj2.person_id = result[0]
    session.add(obj2)
    session.commit()
    obj3.person_id = result[0]
    session.add(obj3)
    session.commit()

# person1 = Person(first_name = 'mayur', dob = '2002-5-3',last_name = 'shah',phone_number = 1098264789,email = 'mayur@gmail.com')
# teacher1 = teacher(salary = 1000,doj = '2021-9-1')
# address1 = address(street='west',city='mumbai',country='usa',postal_code=12)
#
# person2 = Person(first_name = 'raman', dob = '1999-12-1',last_name = 'shah',phone_number = 1024567189,email = 'raman@gmail.com')
# teacher2 = teacher(salary = 2000,doj = '2022-9-1')
# address2 = address(street='east',city='banglore',country='uganda',postal_code=34)
#
# person3 = Person(first_name = 'ashish', dob = '2022-6-1',last_name = 'gupta',phone_number = 1029374657,email = 'ashish@gmail.com')
# teacher3 = teacher(salary = 3000,doj = '2020-9-1')
# address3 = address(street='highway',city='mumbai',country='italy',postal_code=56)
#
# add_teacher(person1,teacher1,address1)
# add_teacher(person2,teacher2,address2)
# add_teacher(person3,teacher3,address3)


"""course.py tables"""


def add_course(obj1,obj2,obj3):
    session.add_all([obj1,obj2,obj3])
    session.commit()

# course1 = Course(title = 'python',credits = 10 ,level=12,total = 10)
# course2 = Course(title = 'java',credits = 15 ,level=13 ,total = 15)
# course3 = Course(title = 'mysql',credits = 20 ,level=14, total = 20)
# course4 = Course(title = 'dsa',credits = 20 ,level=15, total = 20)
# course5 = Course(title = 'spa',credits = 15 ,level=14, total = 15)
# course6 = Course(title = 'c++',credits = 20 ,level=15, total = 20)
# add_course(course4,course5,course6)



def add_exam(obj1,obj2,obj3):
    session.add_all([obj1,obj2,obj3])
    session.commit()
# exam1 = Exam(exam_date = '2022-5-20',supervisor = 'sarika',total_marks = 80)
# exam2 = Exam(exam_date = '2022-5-25',supervisor = 'saurabh',total_marks = 80)
# exam3 = Exam(exam_date = '2022-5-30',supervisor = 'prajakta',total_marks = 80)


# add_exam(exam1,exam2,exam3)



"""enrollment.py tables"""


# def enroll_stud():
#     s = session.query(Student)
#     c = session.query(Course)
#
#
#
#
#
# enroll_stud()


"""update operation"""
# def up(class_name,col_name,new_value,cl_col,olprint(df2)d_value):
#     u = update(class_name)
#     u = u.values({col_name: new_value})
#     u = u.where(cl_col == old_value)
#     cnx.execute(u)
# up(Person,'first_name','semil',Person.first_name,'nilesh')