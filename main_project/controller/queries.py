#This file is used to store all the queries

"""enrollment.py queries"""
# Taking input from user and enrolling student to course
student_enrollemnt = ('insert into enrollment (enroll_course_id,student_id) select course.course_id, student.id from student inner join course on student.student_level = course.level where not exists (select enroll_course_id,student_id from enrollment where enroll_course_id = %s and student_id= %s)  and  course.course_id = %s and student.id = %s;' )
# To get count of students enrolled into a course
student_count_enrolled_into_course = ('SELECT COUNT(enroll_course_id) AS freq FROM enrollment where student_id = %s;' )
# To get distinct students taught by each professor
get_distinct_student = ('select count(distinct student_id) as frequency from enrollment inner join course on enroll_course_id=course_id where emp_id = %s;')

"""task5.py queries"""
# inserting into attempt table
insert_into_attempt = ("INSERT INTO attempt (student_id,exam_id,student_marks) VALUES (%s,%s,%s);")
# Count of total student passed in exam
passed = ("SELECT COUNT(student_marks) from attempt where student_marks>35;")
# Count of total student failed in exam
failed = ("SELECT COUNT(student_marks) from attempt where student_marks<35;")
# Average marks of student
average = ("select avg(student_marks) from attempt;")
# getting percentage of students who passed the exam and percentage of student who failed the exam
percentage = ("select count(student_marks) from attempt")