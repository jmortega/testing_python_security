#!/usr/bin/python3

import sqlite3
db = "students.db"
conn = sqlite3.connect(db)
c = conn.cursor()

cmd = "CREATE TABLE students (Name TEXT, Age INT)"
c.execute(cmd)
conn.commit()

data = [("Robert", 10), ("Sally", 15), ("Matthew", 7)]
 
#For avoid sql injection the best practice is using the ? character (instead of %s) to pass in values. 
#This way, SqLite will escape any special characters we put in.
 
c.executemany("INSERT INTO students VALUES (?,?)", data)
conn.commit()

c.execute("SELECT * from students WHERE Name='Robert'")
result = c.fetchall()
print(result)

data = [("Robert'; DROP TABLE students;--", 10)]
c.executemany("INSERT INTO students VALUES (?,?)", data)
conn.commit()

Name = "Robert'; DROP TABLE students;--"
Name_to_use = (Name,)
print("SELECT * from students WHERE Name=(?)" , Name_to_use)

c.execute("SELECT * from students WHERE Name=(?)" , Name_to_use)
 
result = c.fetchall()
print(result)

