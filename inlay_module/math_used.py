import math, random

print(math.cos(math.pi / 4))

print(math.log(1024, 2))


choiceFruit = random.choice(['apple','pear', 'banana'])
print(choiceFruit)
rangeRandom = random.sample(range(100), 10)
print(rangeRandom)
print(random.random())
print(random.randrange(6))

print("------------------------------------")


from urllib.request import urlopen
for line in urlopen("http://tycho.usno.navy.mil/cgi-bin/timer.pl"):
    line = line.decode('utf-8')
    # if 'EST' in line or 'EDT' in line:
    print(line)