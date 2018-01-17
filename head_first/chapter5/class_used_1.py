from head_first.chapter5.filter_speed_2 import sanitize


class Athlete:
    name = ''
    dob = ''
    times = []
    filename = ''

    def __init__(self, filename=''):
        self.filename = filename

    def top3(self):
        return sorted(set([sanitize(t) for t in self.times]))[0:3]

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

    def add_time(self,time_value):
        self.times.append(time_value)

    def add_times(self,list_of_times):
        self.times.extend(list_of_times)



sarah = Athlete('sarah.txt')
james = Athlete('James Jones')
print(type(sarah))
print(type(james))

print(sarah.get_coach_data().top3())
print(sarah.get_coach_data().name + "'s fastest times are: " +
      str(sarah.get_coach_data().top3()))

sarah.add_time('1.24')
print(sorted(sarah.times))
sarah.add_times(['1.35','2.45'])
print(sorted(sarah.times))