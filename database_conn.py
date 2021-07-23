#!python3

# Python Database API

import sqlite3

con = sqlite3.connect('D:\SQL\Ex_Files_SQL_EssT\Exercise Files\db\world.db')

cursor = con.cursor()

sql1 = 'DROP TABLE IF EXISTS EMPLOYEE'

sql2 = '''

       CREATE TABLE EMPLOYEE (
       EMPID INT(6) NOT NULL,
       NAME CHAR(20) NOT NULL,
       AGE INT,
       SEX CHAR(1),
       INCOME FLOAT
       )
      '''

# executing sql statements
#cursor.execute(sql1)
#cursor.execute(sql2)

# Inserting Data into Table  execute() : single row, executeMany() : multiple rows

# preparing sql statement
rec = (456789, 'Frodo', 45, 'M', 100000.00)
sql = '''
      INSERT INTO EMPLOYEE VALUES ( ?, ?, ?, ?, ?)
      '''
# executing sql statement using try ... except blocks
try:
    cursor.execute(sql, rec)
    con.commit()

except Exception as e:
    print("Error Message :", str(e))
    con.rollback()

# preparing sql statement

records = [
    (123456, 'John', 25, 'M', 50000.00),
    (234651, 'Juli', 35, 'F', 75000.00),
    (345121, 'Fred', 48, 'M', 125000.00),
    (562412, 'Rosy', 28, 'F', 52000.00)
    ]

sql = '''
       INSERT INTO EMPLOYEE VALUES ( ?, ?, ?, ?, ?)
      '''
try:
    cursor.executemany(sql,records)
    con.commit()
except Exception as e:
    print('Error Message :',str(e))
    con.rollback()

# Fetching data   fetchone() : one record at a time, fetchall() : retrive all [ both in the form of tuples]

sql = '''
       SELECT * FROM EMPLOYEE
      '''

try:
    cursor.execute(sql)
except Exception as e:
    print('Unable to fetch data.')

records = cursor.fetchall()

for  record in records:
    print(record)


# closing the connection
con.close()

# Object Reational Mapper (ORM)  :library that automates the transfer of data stored in relational database tables 
# into objects that are adopted in application code.

'''
Normal Query : SELECT * FROM EMPLOYEE WHERE INCOME=10000.00

Django code : emps = Employee.objects.filter(income=10000.00)

'''

