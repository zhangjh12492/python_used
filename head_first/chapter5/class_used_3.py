from head_first.chapter5.filter_speed_2 import sanitize


class Athlete:
    def __init__(self, a_name, a_dob=None, a_times=[]):
        self.name = a_name
        self.dob = a_dob

    def top3(self):
        return (sorted(set([sanitize(t) for t in self.times])))


class AthleteList(list):
    def __init__(self, a_name, a_dob=None, a_times=[]):
        list.__init__([])
        self.name = a_name
        self.dob = a_dob
        self.extend(a_times)

    def top3(self):
        return (sorted(set([sanitize(t) for t in self])))

vera=AthleteList('vera vi')
vera.append('1.34')
print(vera.top3())
vera.extend(['2.22','1-21','2:22'])
print(vera.top3())