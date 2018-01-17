import pickle
from head_first.chapter5.class_used_1 import Athlete


# pickle.dump
# pickle.load


def get_coach_data(filename):
    print(filename)


def put_to_store(files_list):
    all_athletes = {}
    for each_file in files_list:
        ath_=Athlete(each_file)
        ath = ath_.get_coach_data()
        all_athletes[ath.name] = ath
    try:
        with open('athletes.pickle', 'wb') as athf:
            pickle.dump(all_athletes, athf)
    except IOError as ioerr:
        print('File error(put_to_store):' + str(ioerr))
    return all_athletes


def get_from_store():
    all_athletes = {}
    try:
        with open('athletes.pickle', 'rb') as athf:
            all_athletes = pickle.load(athf)
    except IOError as ioerr:
        print('File error (get_from_store): ' + str(ioerr))
    return all_athletes
print("------------------------------")
files_list=['james.txt','julie.txt']
put_to_store(files_list)

all_athletes=get_from_store()
for ath in all_athletes:
    print(ath)