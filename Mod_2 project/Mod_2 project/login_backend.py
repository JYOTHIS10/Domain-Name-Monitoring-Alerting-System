#!/usr/bin/python3 

import cgi
import cgitb
import hashlib, binascii, os
cgitb.enable()
from jinja2 import Template, Environment, FileSystemLoader

import datetime

print("Content-type: text/html")
print()
print("<br>")
# Create instance of FieldStorage
form_data = cgi.FieldStorage()


email = form_data['email_login'].value
 
password= form_data['password_login'].value



import pymysql
from pymysql.err import MySQLError


conn = pymysql.connect(db='pyb51_gp1', user='pyb51_gp1', passwd='q8sj922s', host='localhost')
c = conn.cursor()
try:
  sql = 'SELECT salt FROM sign_up where email="%s"' %(email)
  c.execute(sql)

  for row in c.fetchall():
    salt = row[0]

    pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), salt.encode('utf-8'), 100000)
    pwdhash = binascii.hexlify(pwdhash)
    password = (salt.encode('utf-8') + pwdhash).decode('ascii')


  sql = 'SELECT email, password FROM sign_up where email="%s" && password="%s"' %(email, password)

  c.execute(sql)
  count = 0
  for row in c.fetchall():
    count = count + 1;

    print("data")

  conn.commit()
  

except MySQLError as e:
  print('Got error {!r}, errno is {}'.format(e, e.args[0]))



if count > 0:
  print("Content-type:text/html\n\n")
  redirectURL = "http://pyb51-gp1.specind.net/user_page.html"  
  print("<html>")
  print("<head>")
  print('<meta http-equiv="refresh" content="0;url='+str(redirectURL)+'" />')
  print("</head>")
  print("<body>")
  print("<p> Welcome! </p")
  print("</body")
  print ("</html>")
else:
  print("Content-type:text/html\n\n")
  redirectURL = "http://pyb51-gp1.specind.net/signup_login.html"  
  print("<html>")
  print("<head>")
  print('<meta http-equiv="refresh" content="0;url='+str(redirectURL)+'" />')
  print("</head>")
  print ("</html>")