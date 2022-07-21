from main_project.model.course import Course,Exam
from main_project.model.person import Person,Student,teacher,address
from main_project.controller.crud import add_stud,add_teacher,add_course,add_exam,up
from main_project.model.enroll_and_exam import Enrollments

"""below line is used to add student into student table"""

# person1 = Person(first_name = 'suresh', dob = '2021-6-3',last_name = 'bariya',phone_number = 10981339,email = 'suresh@gmail.com')
# student1 = Student(roll_number = 2468, batch = 2020,level = 12)
# address1 = address(street='prakashnagar',city='mumbai',country='india',postal_code=419203)
#
# person2 = Person(first_name = 'ayush', dob = '2020-6-3',last_name = 'shah',phone_number = 1029836456,email = 'ayush@gmail.com')
# student2 = Student(roll_number = 1092, batch = 2019,level = 13)
# address2 = address(street='ayushnagar',city='delhi',country='india',postal_code=109283)
#
# person3 = Person(first_name = 'milan', dob = '2018-6-3',last_name = 'bariya',phone_number = 1296758945,email = 'milan@gmail.com')
# student3 = Student(roll_number = 1154, batch = 2020,level=14)
# address3 = address(street='milanhnagar',city='mumbai',country='india',postal_code=61527)
#
# add_stud(person1,student1,address1)
# add_stud(person2,student2,address2)
# add_stud(person3,student3,address3)
# """below code is used to add teacher into teacher table"""
#
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
#
# """below code is used to add course details into course table"""
# course1 = Course(teacher_id = 1,title = 'python',credits = 10 ,level=12,total = 10)
# course2 = Course(teacher_id = 2,title = 'java',credits = 15 ,level=13 ,total = 15)
# course3 = Course(teacher_id = 3,title = 'mysql',credits = 20 ,level=14, total = 20)
# course4 = Course(teacher_id = 1,title = 'dsa',credits = 20 ,level=15, total = 20)
# course5 = Course(teacher_id = 2,title = 'spa',credits = 15 ,level=14, total = 15)
# course6 = Course(teacher_id = 3,title = 'c++',credits = 20 ,level=15, total = 20)
#
# add_course(course1,course2,course3,course4,course5,course6)
#
# """below code is used to add exam details in exam table"""
# exam1 = Exam(exam_date = '2022-5-20',supervisor = 'sarika',total_marks = 80)
# exam2 = Exam(exam_date = '2022-5-25',supervisor = 'saurabh',total_marks = 80)
# exam3 = Exam(exam_date = '2022-5-30',supervisor = 'prajakta',total_marks = 80)
# add_exam(exam1,exam2,exam3)
#
# """below code is used to update details"""
#
# up(class_name,"column_name","new value',"class_name.column_name,old_value)


