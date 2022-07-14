# from sqlalchemy import create_engine
# from sqlalchemy.orm import relationship, backref, sessionmaker
#
# from sqlalchemy.ext.declarative import declarative_base
# Base = declarative_base()
# import sys
#
# sys.path.append( '/home/kushal/Desktop/project')
#
# from connector import cnx
# Session = sessionmaker(bind=cnx)
# session = Session()
#
# import person
# import course
#
#
#
# Base.metadata.create_all(cnx, checkfirst=True)
# Session = sessionmaker(bind=cnx)
# session = Session()
#
# a1 = person.person()
# b1 = course.course()
# b2 = course.course()
# c1 = course.exam()
# c2 = course.exam()
#
# a1.Bs.append(b1)
# a1.Bs.append(b2)
# a1.Cs.append(c1)
# a1.Cs.append(c2)
# session.add(a1)
#
# person1 = person.person(first_name = 'semil', dob = '2000-9-12',last_name = 'shah',phone_number = 73,email = 'shahsemil2@gmail.com')
# session.add(person1)
# session.commit()
# #person1 = person(first_name = 'semil', dob = 12-9-2000,last_name = 'shah',phone_number = 7021109502,email = 'shahsemil2@gmail.com')