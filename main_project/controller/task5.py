from sqlalchemy import text
from main_project.model.base import session,cnx
from main_project.model.course import Exam

def get_exam_id(exam_id):
    result = session.query(Exam).filter(Exam.exam_number == exam_id).first()
    return result

# def insert(table_name,column_name,values):


def insert_into_attempt():
    inp_student_id = int(input("add student id"))
    inp_exam_id = int(input("add exam id"))
    inp_student_marks = int(input("add student marks"))
    ed = get_exam_id(exam_id=inp_exam_id)
    if ed.total_marks > inp_student_marks:
        sql = text("INSERT INTO attempt (student_id,exam_id,student_marks) VALUES (%s,%s,%s);"% (inp_student_id,inp_exam_id,inp_student_marks))
        result=cnx.execute(sql)


def total_passed():
    sql = text("SELECT COUNT(student_marks) from attempt where student_marks>35;")
    result = cnx.execute(sql).first()
    return result[0]
    return result[0]

def total_failed():
    sql = text("SELECT COUNT(student_marks) from attempt where student_marks<35;")
    result = cnx.execute(sql).first()
    return result[0]
    return result[0]

def avg_marks():
    sql = text("select avg(student_marks) from attempt;")
    result = cnx.execute(sql).first()
    return result[0]


#to calculate total count of students who attempted exams
total_count = text("select count(student_marks) from attempt")
res = cnx.execute(total_count).first()
t = res[0]
def get_percentage():
    passed = total_passed()
    failed = total_failed()
    total_count = t

    passedPercetage = (passed / t ) * 100
    failedPercentage = 100 - passedPercetage

    return passedPercetage,passedPercetage







