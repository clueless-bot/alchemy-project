from sqlalchemy import create_engine,Column,Integer,String,MetaData,Date
from sqlalchemy.orm import sessionmaker,backref,relationship,backref
from sqlalchemy.ext.declarative import declarative_base
from main_project.model.base import Base
from main_project.model.person import *
from connector import cnx
from main_project.model.base import *
from main_project.model.course import *
from main_project.model.person import *

"""person.py"""

# person1 = Person(first_name = 'semil', dob = '2000-9-12',last_name = 'shah',phone_number = 7021109502,email = 'shahsemil2@gmail.com')
# person2 = Person(first_name = 'henil', dob = '1996-12-1',last_name = 'shah',phone_number = 9773500045,email = 'henilshah89@gmail.com')
# person3 = Person(first_name = 'meet', dob = '2000-6-1',last_name = 'shah',phone_number = 1234567890,email = 'meet@gmail.com')
# session.add_all([person1,person2,person3])
# session.commit()
# our_user = session.query(Person)
# for p in our_user:
#     if p.first_name == 'semil':
#         student_semil = p.id
#     if p.first_name == 'henil':
#         student_henil = p.id
#     if p.first_name == 'meet':
#         student_meet = p.id
#
# # student1 = student(person_id = student_semil,roll_number = 8698, batch = 2022)
# student2 = student(person_id = student_henil,roll_number = 7021, batch = 2021)
# student3 = student(person_id = student_meet,roll_number = 2189, batch = 2020)
# session.add_all([student2,student3])
# session.commit()

# def add_stud(obj1,obj2,obj3):
#     session.add_all([obj1,obj2,obj3])
#     session.commit()
# person1 = Person(first_name = 'semil', dob = '2000-9-12',last_name = 'shah',phone_number = 7021109502,email = 'shahsemil2@gmail.com')
# person2 = Person(first_name = 'henil', dob = '1996-12-1',last_name = 'shah',phone_number = 9773500045,email = 'henilshah89@gmail.com')
# person3 = Person(first_name = 'meet', dob = '2000-6-1',last_name = 'shah',phone_number = 1234567890,email = 'meet@gmail.com')
#
# student1 = student(person_id = 3,roll_number = 8698, batch = 2022)
# student2 = student(person_id = 4,roll_number = 7021, batch = 2021)
# student3 = student(person_id = 5,roll_number = 2189, batch = 2020)
#
# address1 = address(person_id = 3,street='jawaharnagar',city='mumbai',country='india')
# address2 = address(person_id = 4,street='bangur nagar',city='banglore',country='india')
# address3 = address(person_id = 5,street='siddarth nagar',city='mumbai',country='india')

#add_stud(person1,person2,person3)
# add_stud(student1,student2,student3)
# add_stud(address1,address2,address3)

# def add_teacher(obj1,obj2,obj3):
#     session.add_all([obj1,obj2,obj3])
#     session.commit()
# person1 = Person(first_name = 'mayur', dob = '2002-5-3',last_name = 'shah',phone_number = 1098264789,email = 'mayur@gmail.com')
# person2 = Person(first_name = 'ayush', dob = '1999-12-1',last_name = 'shah',phone_number = 1024567189,email = 'ayush@gmail.com')
# person3 = Person(first_name = 'ashish', dob = '2022-6-1',last_name = 'gupta',phone_number = 1029374657,email = 'ashish@gmail.com')
#
# teacher1 = teacher(salary = 1000,person_id = 7,doj = '2021-9-1')
# teacher2 = teacher(salary = 2000,person_id = 8,doj = '2021-9-1')
# teacher3 = teacher(salary = 3000,person_id = 9,doj = '2021-9-1')
#
# address1 = address(person_id = 7,street='west',city='mumbai',country='usa',postal_code=12)
# address2 = address(person_id = 8,street='east',city='banglore',country='uganda',postal_code=34)
# address3 = address(person_id = 9,street='highway',city='mumbai',country='italy',postal_code=56)
#
# add_teacher(person1,person2,person3)
# add_teacher(teacher1,teacher2,teacher3)
# add_teacher(address1,address2,address3)


"""course.py"""

# def add_course(obj1,obj2,obj3):
#     session.add_all([obj1,obj2,obj3])
#     session.commit()
# course1 = Course(person_id = 3,title = 'python',credits = ,level=12,total=)
# course2 = Course(person_id = 4,title = 'java',credits = ,level=13,total=)
# course3 = Course(person_id = 5,title = 'java',credits = ,level=13,total=)
#
# add_course(course1,course2,course3)

# def add_exam(obj1,obj2,obj3):
#     session.add_all([obj1,obj2,obj3])
#     session.commit()
#
# exam1 = Exam(person_id = 3,exam_date = '2022-5-20',supervisor = 'sarika',total_marks = 80)
# exam2 = Exam(person_id = 4,exam_date = '2022-5-25',supervisor = 'saurabh',total_marks = 80)
# exam3 = Exam(person_id = 5,exam_date = '2022-5-30',supervisor = 'prajakta',total_marks = 80)
#
# add_exam(exam1,exam2,exam3)


"""Update Operation"""


# def up(class_name,col_name,new_value,cl_col,old_value):
#     u = update(class_name)
#     u = u.values({col_name: new_value})
#     u = u.where(cl_col == old_value)
#     cnx.execute(u)
# up(Person,'first_name','semil',Person.first_name,'nilesh')