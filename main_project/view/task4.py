from main_project.controller.enrollment import student_enrollment_course,get_student_count_enrolled_into_course,get_distinct_students
import logging
logging.basicConfig(filename="enrollment.log",level=logging.INFO)
# enroll student into particular course
enroll = student_enrollment_course()

#count of student enrolled into particular course
count_enroll = get_student_count_enrolled_into_course()
logging.info(count_enroll)

# count distinct students taught by single professor
distinct_student = get_distinct_students()
logging.info(distinct_student)
