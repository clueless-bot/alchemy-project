from sqlalchemy import text
from main_project.model.base import cnx,session
from main_project.model.course import Exam
from main_project.controller.queries import insert_into_attempt,passed,failed,average,percentage
from main_project.model.enroll_and_exam import Enrollments

def get_exam_id(exam_id):
    result = session.query(Exam).filter(Exam.exam_number == exam_id).first()
    return result

def insert(table_name,column_names,values):
    inp_exam = int(input("add exam id to get total marks :"))
    inp_marks = int(input("add marks to verify if it can be added to table or not :"))
    ed = get_exam_id(exam_id=inp_exam)
    if ed.total_marks > inp_marks:
        sep = ","
        sql = text("INSERT INTO "+table_name +"(" +sep.join(column_names)+") " +"VALUES "+ "(" + sep.join(values) + ")")
        result = cnx.execute(sql)
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
    """getting percentage of students who passed the exam and percentage of student who failed the exam"""
    total_count = text(percentage)
    res = cnx.execute(total_count).first()
    t = res[0]
    passed = total_passed()
    failed = total_failed()
    total_count = t

    passedPercetage = (passed / t ) * 100
    failedPercentage = 100 - passedPercetage

    return passedPercetage,failedPercentage








