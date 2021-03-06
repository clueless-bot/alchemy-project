import json
from sqlalchemy import create_engine

with open('/home/kushal/Desktop/project/config.json') as config:
    data = json.load(config)
    user = data["username"]
    password = data["password"]
    db = data["database"]
    port = data['host']

cnx = create_engine("mysql+pymysql://"+user+":"+password+"@localhost:"+port+"/"+db+"?charset=utf8mb4")

