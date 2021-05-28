import pymysql
import hashlib

db = pymysql.connect(host = 'localhost', user = 'root', passwd = 'shalom1966', db = 'stan')

mydb = db.cursor()


















db.commit()
db.close()