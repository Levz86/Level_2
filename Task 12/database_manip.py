import sqlite3

db = sqlite3.connect ('database_db')
#create the table python_programming
cursor = db.cursor()
cursor.execute(''' CREATE TABLE python_programming(id INTEGER PRIMARY KEY,
 name TEXT, grade INTERGER)''')

id = '55'
name = 'Carl Davis'
grade = '61'

id2 = '66'
name2 = 'Dennis Fredrickson'
grade2 = '88'

id3 = '77'
name3 = 'Jane Richards'
grade3 = '78'

id4 = '12'
name4 = 'Peyton Sawyer'
grade4 = '45'

id5 = '2'
name5 = 'Locas Brooke'
grade5 = '99'

#insert the new rows into the python_programming table
cursor.execute(''' INSERT INTO python_programming(id, name, grade)VALUES(?,?,?)''',(id,name,grade))

cursor.execute(''' INSERT INTO python_programming(id, name, grade)VALUES(?,?,?)''',(id2,name2,grade2))

cursor.execute(''' INSERT INTO python_programming(id, name, grade)VALUES(?,?,?)''',(id3,name3,grade3))

cursor.execute(''' INSERT INTO python_programming(id, name, grade)VALUES(?,?,?)''',(id4,name4,grade4))

cursor.execute(''' INSERT INTO python_programming(id, name, grade)VALUES(?,?,?)''',(id5,name5,grade5))
print('All users inserted')

#select all records with a grade between 60 and 80
cursor.execute('''SELECT id, name FROM python_programming WHERE grade BETWEEN 60 AND 80''')
rows = cursor.fetchall()
for row in rows:
    print(rows)

#change carl davis grade to 65
cursor.execute("UPDATE python_programming SET grade = 65 WHERE name = 'Carl Davis'")
print ('Carl Davis grade has been updates')

#delete dennis fredricksons row
cursor.execute("DELETE FROM python_programming WHERE id = 'Dennis Fredrickson'")
print ('Dennis Fredricksons has been deleted')

#change the grade for all people with an id below than 55
cursor.execute('''UPDATE python_programming SET grade = 60 WHERE id < 55''')
print ('Grades changed')

db.commit()
db.close()
