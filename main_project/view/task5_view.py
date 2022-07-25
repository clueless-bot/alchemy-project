from main_project.controller.task5 import total_passed,total_failed,avg_marks,get_percentage,insert
from main_project.model.enroll_and_exam import Enrollments
import logging
logging.basicConfig(filename="task5.log",level=logging.INFO)


"""below code is used to add values to attempt table"""
table_name = "attempt "
column_names = ['student_id','exam_id','student_marks']
inp_student_id = str(input("add student id"))
inp_exam_id = str(input("add exam id"))
inp_student_marks = str(input("add student marks"))
values = [inp_student_id,inp_exam_id,inp_student_marks]

insert(table_name,column_names,values)

"""below code is used to check total student who passed the exam"""
passed = total_passed()
logging.info(passed)

"""below code is used to check total student who failed the exam"""
failed = total_failed()
logging.info(failed)

"""below code is used to find average marks of all student"""
average = avg_marks()
logging.info(average)
"""below code is used to find pass percentage and fail percentage"""
percentage = get_percentage()
logging.info(percentage)