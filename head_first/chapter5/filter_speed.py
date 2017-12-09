import os

os.chdir("./")

print(os.getcwd())


def sanitize(time_string):
    if "-" in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return time_string
    (mins, secs) = time_string.split(splitter)
    return (mins + '.' + secs)


with open('james.txt') as jam:
    data = jam.readline()
james = data.strip("").split(",")

with open('julie.txt') as jul:
    data = jul.readline()
julie = data.strip().split(",")

with open('mikey.txt') as mik:
    data = mik.readline()
mikey = data.strip().split(",")

with open('sarah.txt') as sar:
    data = sar.readline()
sarah = data.strip().split(",")
print("\n\n")

clean_james = []
clean_julie = []
clean_mikey = []
clean_sarah = []

for each_t in james:
    clean_james.append(sanitize(each_t))
for each_t in julie:
    clean_julie.append(sanitize(each_t))
for each_t in mikey:
    clean_mikey.append(sanitize(each_t))
for each_t in sarah:
    clean_sarah.append(sanitize(each_t))

print(set(sorted(clean_james, reverse=True)))
print(set(sorted(clean_julie)))
print(sorted(clean_mikey))
print(sorted(clean_sarah))


print('\n\n\n')
clean_james=[sanitize(each_t) for each_t in james]
print(sorted(clean_james))

print("\n")
dirty=['2-22','2:22','2.22']
clean=[sanitize(d) for d in dirty]
print(clean)
clean=[float(sanitize(d)) for d in dirty]
print(clean)

print("\n\n")
print(sorted([sanitize(j) for j in james]))
clean_james=sorted([sanitize(j) for j in set(james)])
print(clean_james[0:3])


