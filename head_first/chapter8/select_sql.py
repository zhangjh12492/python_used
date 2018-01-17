import sqlite3

connection = sqlite3.connect('coachdata.sqlite')
cursor = connection.cursor()
name = 'james'
dob = '2002-6-17'
cursor.execute('SELECT id FROM athletes WHERE name=?', (name,))

the_current_id = cursor.fetchone()[0]
print(the_current_id)
