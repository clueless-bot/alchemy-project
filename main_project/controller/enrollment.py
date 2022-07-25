from sqlalchemy import text
from main_project.model.base import cnx
from main_project.controller.queries import student_count_enrolled_into_course,student_enrollemnt,get_distinct_student


def student_enrollment_course() -> None:
    """Taking input from user and enrolling student to course"""
    inp_student_id = int(input('Enter student id:'))
    inp_course_id = int(input('Enter course id:'))
    sql = text(student_enrollemnt % (inp_course_id,inp_student_id,inp_course_id,inp_student_id))
    results = cnx.execute(sql)

def get_student_count_enrolled_into_course() -> int:
    """To get count of students enrolled into a course"""
    inp_student_id = int(input("Enter student id to find count of students"))
    sql = text(student_count_enrolled_into_course % (inp_student_id))
    results = cnx.execute(sql).first()
    return results[0]

def get_distinct_students() -> int:
    """To get distinct students taught by each professor"""
    inp_emp_id = int(input("Enter employee id to find count of distinct students:"))
    sql = text(get_distinct_student % (inp_emp_id))
    results = cnx.execute(sql).first()
    return results[0]
