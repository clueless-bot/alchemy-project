from sqlalchemy import text
from main_project.model.base import session,cnx
from main_project.model.course import Exam
from main_project.controller.queries import insert_into_attempt,passed,failed,average,percentage

def get_exam_id(exam_id):
    result = session.query(Exam).filter(Exam.exam_number == exam_id).first()
    return result


def insert_into_attempt():
    """inserting into attempt table"""
    inp_student_id = int(input("add student id"))
    inp_exam_id = int(input("add exam id"))
    inp_student_marks = int(input("add student marks"))
    ed = get_exam_id(exam_id=inp_exam_id)
    if ed.total_marks > inp_student_marks:
        sql = text(insert_into_attempt % (inp_student_id,inp_exam_id,inp_student_marks))
        result=cnx.execute(sql)


def total_passed() -> None:
    """Count of total student passed in exam"""
    sql = text(passed)
    result = cnx.execute(sql).first()
    return result[0]

def total_failed() -> int:
    """Count of total student failed in exam"""
    sql = text(failed)
    result = cnx.execute(sql).first()
    return result[0]

def avg_marks() -> int:
    """Average marks of student"""
    sql = text(average)
    result = cnx.execute(sql).first()
    return result[0]


#to calculate total count of students who attempted exams
def get_percentage() -> float:
    """getting total students who passed the exam and total total student who failed the exam"""
    total_count = text(percentage)
    res = cnx.execute(total_count).first()
    t = res[0]
    passed = total_passed()
    failed = total_failed()
    total_count = t

    passedPercetage = (passed / t ) * 100
    failedPercentage = 100 - passedPercetage

    return passedPercetage,failedPercentage








