from sqlalchemy import text
from main_project.model.base import cnx
from main_project.model.enroll_and_exam import Enrollments

#Taking input from user and enrolling student to course
def student_enrollment_course():
    inp_student_id = int(input('Enter student id:'))
    inp_course_id = int(input('Enter course id:'))
    sql = text('insert into enrollment (enroll_course_id,student_id) select course.course_id, student.id from student inner join course on student.student_level = course.level where not exists (select enroll_course_id,student_id from enrollment where enroll_course_id = %s and student_id= %s)  and  course.course_id = %s and student.id = %s;' % (inp_course_id,inp_student_id,inp_course_id,inp_student_id))
    results = cnx.execute(sql)

def get_student_count_enrolled_into_course():
    inp_student_id = int(input("Enter student id to find count of students"))
    sql = text('SELECT COUNT(enroll_course_id) AS freq FROM enrollment where student_id = %s;' % (inp_student_id))
    results = cnx.execute(sql)
    for i in results:
        print(i[0])

def get_distinct_students():
    inp_emp_id = int(input("Enter employee id to find count of distinct students:"))
    sql = text('select count(distinct student_id) as frequency from enrollment inner join course on enroll_course_id=course_id where emp_id = %s;' % (inp_emp_id))
    results = cnx.execute(sql)
    for i in results:
        print(i[0])



