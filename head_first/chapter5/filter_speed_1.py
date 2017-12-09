import os


def get_file_datas(file_name):
    try:
        with open(file_name) as jam:
            data = jam.readline()
        return data.strip().split(",")
    except IOError as ioerr:
        print('file error:' + str(ioerr))
        return None


def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return (time_string)
    (mins, secs) = time_string.split(splitter)
    return (mins + "." + secs)


james = get_file_datas('james.txt')
julie = get_file_datas('julie.txt')

print(sorted(set([sanitize(j) for j in james]))[0:3])
print(sorted([sanitize(j) for j in julie]))
