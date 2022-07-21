from sqlalchemy import *
from main_project.model.base import *
from main_project.model.course import *
from main_project.model.person import *
from main_project.controller.enrollment import *


"""below line is used to add student into student table"""

# add_stud(person1,student1,address1)
# add_stud(person2,student2,address2)
# add_stud(person3,student3,address3)
"""below code is used to add teacher into teacher table"""

# add_teacher(person1,teacher1,address1)
# add_teacher(person2,teacher2,address2)
# add_teacher(person3,teacher3,address3)

"""below code is used to add course details into course table"""

# add_course(course1,course2,course3)

"""below code is used to add exam details in exam table"""

# add_exam(exam1,exam2,exam3)
"""below code is used to update details"""
# up(class_name,"column_name","new value',"class_name.column_name,old_value)

"""below 3 commands are used to fetch
1)enroll student into particular course
2)count of student enrolled into particular course
3)count distinct students taught by single professor
"""
# student_enrollment_course()
# get_student_count_enrolled_into_course()
# get_distinct_students()
