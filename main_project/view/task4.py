from main_project.controller.enrollment import student_enrollment_course,get_student_count_enrolled_into_course,get_distinct_students

# enroll student into particular course
inp_student_id = int(input('Enter student id:'))
inp_course_id = int(input('Enter course id:'))

student_enrollment_course(inp_student_id,inp_course_id)

#count of student enrolled into particular course
get_student_count_enrolled_into_course()

# count distinct students taught by single professor
get_distinct_students()