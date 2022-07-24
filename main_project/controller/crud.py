from main_project.model.base import session,cnx
from main_project.model.person import Person
from sqlalchemy import update

#Person.py Table
def add_stud(person,student,address):
    """Adding student details"""
    session.add(person)
    session.commit()
    result = session.query(Person) \
        .with_entities(student.id) \
        .filter(Person.email == person.email).first()
    student.person_id = result[0]
    session.add(student)
    session.commit()
    student.person_id = result[0]
    session.add(address)
    session.commit()


def add_teacher(person,teacher,address):
    """adding teacher details"""
    session.add(person)
    session.commit()
    result = session.query(Person) \
        .with_entities(person.id) \
        .filter(Person.email == person.email).first()
    teacher.person_id = result[0]
    session.add(teacher)
    session.commit()
    address.person_id = result[0]
    session.add(address)
    session.commit()

#course.py tables
def add_course(course1,course2,couurse3,course4,course5,course6):
    """adding course"""
    session.add_all([course1,course2,couurse3,course4,course5,course6])
    session.commit()

def add_exam(exam1,exam2,exam3):
    """adding exam"""
    session.add_all([exam1,exam2,exam3])
    session.commit()


def up(class_name,col_name,new_value,cl_col,old_value):
    """update operation"""
    u = update(class_name)
    u = u.values({col_name: new_value})
    u = u.where(cl_col == old_value)
    cnx.execute(u)