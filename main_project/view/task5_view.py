from main_project.controller.task5 import get_exam_id,insert_into_attempt,total_passed,total_failed,avg_marks,get_percentage
from main_project.model.enroll_and_exam import Enrollments
import logging
logging.basicConfig(filename="task5.log",level=logging.INFO)


"""below code is used to add values to attempt table"""
insert_into_attempt()

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