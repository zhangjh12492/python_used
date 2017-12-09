def get_file_data(file_name):
    try:
        with open(file_name) as file:
            data = file.readline()
        templ = data.strip().split(",")
        return templ
    except IOError as ioerr:
        print('File error:' + str(ioerr))
        return (None)


def get_coach_data(filename):
    try:
        with open(filename) as file:
            data = file.readline()
        templ = data.strip().split(",")
        return ({
            'NAME': templ.pop(0),
            'DOB': templ.pop(0),
            'Times': templ
        })
    except IOError as ioerr:
        print('File error:' + str(ioerr))
        return (None)


def sanitize(time_strint):
    if '-' in time_strint:
        splitter = '-'
    elif ':' in time_strint:
        splitter = ':'
    else:
        return (time_strint)
    (mins, secs) = time_strint.split(splitter)
    return (mins + '.' + secs)


james_data = get_coach_data('james.txt')

print(james_data['NAME'] + "'s fastest times are: " +
      str(sorted(set([sanitize(t) for t in james_data['Times']]))[0:3]))


class Athlete:
    def __init__(self, value=0):
        # The code to initialize a 'Athlete' object
        self.thing = value

    def how_big(self):
        return (len(self.thing))


a = Athlete()
b = Athlete()
c = Athlete()
d = Athlete('Hello Grail')
print(d.how_big())
