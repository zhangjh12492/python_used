from head_first.chapter5.filter_speed_2 import sanitize


class Athlete:
    def __init__(self, a_name, a_dob=None, a_times=[], filename=''):
        self.name = a_name
        self.dob = a_dob
        self.times = a_times
        self.filename = filename

    def top3(self):
        return sorted(set([sanitize(t) for t in self.times]))[0:3]

    def get_coach_data(self):
        try:
            with open(self.filename) as file:
                data = file.readline()
            templ = data.strip().split(",")
            self.times = templ[2:-1]
            return self
        except IOError as ioerr:
            print('File error:' + str(ioerr))
            return None


sarah = Athlete('Sarah Sweeney', '2002-6-17', ['2:58', '2.58', '1.56'], 'sarah.txt')
james = Athlete('James Jones')
print(type(sarah))
print(type(james))

print(sarah.get_coach_data().top3())
