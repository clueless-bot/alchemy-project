from sqlalchemy import text
from main_project.model.base import cnx


def student_enrollment_course(inp_student_id,inp_course_id):
    """Taking input from user and enrolling student to course"""
    sql = text('insert into enrollment (enroll_course_id,student_id) select course.course_id, student.id from student inner join course on student.student_level = course.level where not exists (select enroll_course_id,student_id from enrollment where enroll_course_id = %s and student_id= %s)  and  course.course_id = %s and student.id = %s;' % (inp_course_id,inp_student_id,inp_course_id,inp_student_id))
    results = cnx.execute(sql)

def get_student_count_enrolled_into_course():
    """To get count of students enrolled into a course"""
    inp_student_id = int(input("Enter student id to find count of students"))
    sql = text('SELECT COUNT(enroll_course_id) AS freq FROM enrollment where student_id = %s;' % (inp_student_id))
    results = cnx.execute(sql).first()
    return results[0]

def get_distinct_students():
    """To get distinct students taught by each professor"""
    inp_emp_id = int(input("Enter employee id to find count of distinct students:"))
    sql = text('select count(distinct student_id) as frequency from enrollment inner join course on enroll_course_id=course_id where emp_id = %s;' % (inp_emp_id))
    results = cnx.execute(sql).first()
    return results[0]


