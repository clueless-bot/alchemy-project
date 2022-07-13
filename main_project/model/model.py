from sqlalchemy import create_engine
from sqlalchemy.orm import relationship, backref, sessionmaker

import base
import sys

sys.path.append( '/home/kushal/Desktop/project')

from connector import cnx
Session = sessionmaker(bind=cnx)
session = Session()

import person
import course



base.Base.metadata.create_all(cnx, checkfirst=True)
Session = sessionmaker(bind=cnx)
session = Session()

a1 = person.person()
b1 = course.course()
b2 = course.course()
c1 = course.exam()
c2 = course.exam()

a1.Bs.append(b1)
a1.Bs.append(b2)
a1.Cs.append(c1)
a1.Cs.append(c2)
session.add(a1)
session.commit()