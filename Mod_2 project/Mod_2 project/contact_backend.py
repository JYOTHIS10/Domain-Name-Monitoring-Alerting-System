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

name = form_data['name'].value

email = form_data['email'].value

message = form_data['textmessage'].value


import pymysql
from pymysql.err import MySQLError

conn = pymysql.connect(db='pyb51_gp1', user='pyb51_gp1', passwd='q8sj922s', host='localhost')
c = conn.cursor()


try:
  # Execute the SQL command
  sql = 'INSERT INTO contact_form(name, email, message) VALUES ("%s","%s","%s")' %(name, email, message)
  # Commit your changes in the database
  c.execute(sql)
  print("New record inserted successfully")
  conn.commit()

except MySQLError as e:
  print('Got error {!r}, errno is {}'.format(e, e.args[0])) 
  

env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template('output2.html')
output_from_parsed_template = template.render(text_message = textmessage,)    #ask mentor on this part

try:
  fh = open("output1.html", "w")
  fh.write(output_from_parsed_template)
except IOError:
  print ("<br>Error: can't find file or read data")
else:
  print ("Written content in the file successfully")

print("Content-type:text/html\n\n")
redirectURL = "http://pyb51-gp1.specind.net/contact_form.html"  
print("<html>")
print("<head>")
print('<meta http-equiv="refresh" content="0;url='+str(redirectURL)+'" />')
print("</head>")
print ("</html>")

