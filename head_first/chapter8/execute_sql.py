import sqlite3
import pickle
import glob

connection = sqlite3.connect('coachdata.sqlite')
cursor = connection.cursor()


class Athlete:
    name = ''
    dob = ''
    times = []
    filename = ''

    def __init__(self, filename=''):
        self.filename = filename

    def get_coach_data(self):
        try:
            with open(self.filename) as file:
                data = file.readline()
            templ = data.strip().split(",")
            self.name = templ.pop(0)
            self.dob = templ.pop(0)
            self.times = templ
            return self
        except IOError as ioerr:
            print('File error:' + str(ioerr))
            return None


def put_to_store(files_list):
    all_athletes = {}
    for each_file in files_list:
        athle = Athlete(each_file)
        ath = athle.get_coach_data()
        all_athletes[ath.name] = ath
    # try:
    #     with open('athletes.pickle', 'wb') as athf:
    #         pickle.dump(all_athletes, athf)
    # except IOError as ioerr:
    #     print('File error(put_to_store):' + str(ioerr))
    return all_athletes


data_files = glob.glob("*.txt")
athletes = put_to_store(data_files)
print(str(athletes))
for each_ath in athletes:
    name = athletes[each_ath].name
    dob = athletes[each_ath].dob
    cursor.execute("INSERT INTO athletes(name,dob) VALUES (?,?)",(name,dob))
    connection.commit()
connection.close()


# for each_ath in athletes:
#     name =athletes[each_ath].name
#     dob=athletes[each_ath].dob
#     cursor.execute('INSERT INTO athletes(name,dob) VALUES (?,?)', (name, dob))
#     connection.commit()
# connection.close()


# def get_coach_data(filename):
#     try:
#         with open(filename) as f:
#             data = f.readline()
#         templ = data.strip().split(",")
#         return ({
#             'name': templ.pop(0),
#             'dob': templ.pop(0),
#             'times': templ
#         })
#     except IOError as ioerr:
#         print("File error:" + str(ioerr))
#         return (None)
