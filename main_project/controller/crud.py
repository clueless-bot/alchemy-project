from main_project.model.base import session,cnx
from main_project.model.person import Person
from sqlalchemy import update


"""person.py tables"""
def add_stud(obj1,obj2,obj3):
    session.add(obj1)
    session.commit()
    result = session.query(Person) \
        .with_entities(obj1.id) \
        .filter(Person.email == obj1.email).first()
    obj2.person_id = result[0]
    session.add(obj2)
    session.commit()
    obj3.person_id = result[0]
    session.add(obj3)
    session.commit()

def add_teacher(obj1,obj2,obj3):
    session.add(obj1)
    session.commit()
    result = session.query(Person) \
        .with_entities(obj1.id) \
        .filter(Person.email == obj1.email).first()
    obj2.person_id = result[0]
    session.add(obj2)
    session.commit()
    obj3.person_id = result[0]
    session.add(obj3)
    session.commit()



"""course.py tables"""

def add_course(obj1,obj2,obj3):
    session.add_all([obj1,obj2,obj3])
    session.commit()

def add_exam(obj1,obj2,obj3,obj4,obj5,obj6):
    session.add_all([obj1,obj2,obj3,obj4,obj5,obj6])
    session.commit()


# """update operation"""
# def up(class_name,col_name,new_value,cl_col,old_value):
#     u = update(class_name)
#     u = u.values({col_name: new_value})
#     u = u.where(cl_col == old_value)
#     cnx.execute(u)