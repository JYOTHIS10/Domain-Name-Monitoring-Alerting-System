#!/usr/bin/python3 

import cgi
import cgitb
import hashlib, binascii, os
cgitb.enable()
from jinja2 import Template, Environment, FileSystemLoader

print("Content-type: text/html")
print()
print("<br>")
# Create instance of FieldStorage
form_data = cgi.FieldStorage()

# Get data from fields

#userid= form_data["uid"].value

#if form_data['fname'].value:
name = form_data['fname'].value
 # print("Hello, ('%s')" %name)
# else:
  # name = "Name isn't entered"

# if form_data['email'].value:
email = form_data['email'].value
  # print("Your email address is: ('%s')" %email)
# else:
  # email = "Email isn't entered"

# if form_data['password'].value:
password = form_data['password'].value
  # print("Your password is: ('%s')" %password)
# else:
  # password = "Password isn't entered"



# name = form_data["fname"].value

# print("Name of the user is:", name)
# username = form_data["uname"].value                  just commented
# mobile_number = form_data["mnumber"].values          just commented
# email= form_data["email"].value
# print("Email of the user is:", email)

# password = form_data["password"].value
# print("Password of the user is:", password)
#userstatus= form_data["user_status"].value
#user_createddate= form_data["user_created_date"].value
#user_updateddate= form_data["user_updated_date"].value


import pymysql
from pymysql.err import MySQLError
# password1 = form_data["pwd"].value
# salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
# pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), 
#                                 salt, 100000)
# print('pwd',pwdhash)
# pwdhash = binascii.hexlify(pwdhash)
# pwdhash1= pwdhash

def hash_password(password):
  salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
  pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'),salt, 100000)
  pwdhash = binascii.hexlify(pwdhash)
  return (salt + pwdhash).decode('ascii')

new_password = hash_password(password)
salt = new_password[:64]




conn = pymysql.connect(db='pyb51_gp1', user='pyb51_gp1', passwd='q8sj922s', host='localhost')
c = conn.cursor()

#userid= form_data["uid"].value
# name = form_data["fname"].value
# username = form_data["uname"].value
# mobile_number = form_data["mnumber"].value
# email= form_data["email"].value
password= new_password
#userstatus= form_data["user_status"].value
#user_createddate= form_data["user_created_date"].value
#user_updateddate= form_data["user_updated_date"].value
salt1 = salt


try:
  # environ={'REQUEST_METHOD':'POST'}
  # Execute the SQL command
  # c.execute(sql)
  sql = 'INSERT INTO sign_up(name, email, password, salt) VALUES ("%s","%s","%s","%s")' %(name, email, password, salt1)
  # print(sql)
  # c.execute('insert into user values("%s", "%s","%s", "%s","%s", "%s")' % \
  #          (id, name,address,mobile,pwd,salt1))
  # Commit your changes in the database
  c.execute(sql)
  print("New record inserted successfully")
  conn.commit()

except MySQLError as e:
  print('Got error {!r}, errno is {}'.format(e, e.args[0])) 
  

env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template('output.html')
output_from_parsed_template = template.render(salt=salt1,new_password=password,)

try:
  fh = open("output.html", "w")
  fh.write(output_from_parsed_template)
except IOError:
  print ("<br>Error: can't find file or read data")
else:
  print ("Written content in the file successfully")

print("Content-type:text/html\n\n")
redirectURL = "http://pyb51-gp1.specind.net/user_page.html"  
print("<html>")
print("<head>")
print('<meta http-equiv="refresh" content="0;url='+str(redirectURL)+'" />')
print("</head>")
print ("</html>")

