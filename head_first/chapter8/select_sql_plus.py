import sqlite3

db_name = 'coachdata.sqlite'


def get_names_from_store():
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    results = cursor.execute('''SELECT name From athletes''')
    response = [row[0] for row in results]
    connection.close()
    return (response)


def get_namesID_from_store():
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    result = cursor.execute('select id,name from athletes')
    response = result.fetchall()
    connection.close()
    return response


def get_athlete_from_id(athlete_id):
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    results = cursor.execute("""select name,dob from
    athletes WHERE id=?""", (athlete_id,))
    (name, dob) = results.fetchone()
    results = cursor.execute("""select value from timing_data WHERE athlete_id =?""",
                             (athlete_id,))
    data = [row[0] for row in results]
    response = {
        'Name': name,
        'dob': dob,
        'data': data,
        'top3': data[0:3]
    }
    connection.close()
    return (response)


print(get_athlete_from_id(2))

print(get_names_from_store())

print(get_namesID_from_store())
