from sqlalchemy import *
from sqlalchemy.orm import sessionmaker,backref,relationship,backref
from sqlalchemy.ext.declarative import declarative_base
from main_project.model.base import Base
from main_project.model.person import *
from connector import cnx
from main_project.model.base import *
from main_project.model.course import *
from main_project.model.person import *

import pandas as pd
# def show_crud(table):
#     user_table = pd.read_sql_table(table_name=table, con=cnx)
#     print(user_table)
# show_crud('exam')

