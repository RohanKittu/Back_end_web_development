'''
This tutorial you to get some knowledge of data base connectivity
data base connectivity basics

The code presents these topics

- Introduction to python and MYSQL
- Integerated connection
- How to connect pyhon with MYSQL Db
- Perform CURD operations with python and MYSQL 
'''

#Introduction to python and MYSQL
import mysql.connector
#mydb=mysql.connector.connect(host="localhost",user="root",passwd="Kittu@201995")

#print(mydb)
cnx = mysql.connector.connect(host='127.0.0.1',auth_plugin='mysql_native_password')
print(cnx)