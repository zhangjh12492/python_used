import sqlite3

connection = sqlite3.connect('test.sqlite')

cursor = connection.cursor()
cursor.execute("select date('NOW')")
select_result=cursor.fetchone()[0]
print(select_result)
connection.commit()
connection.close()

