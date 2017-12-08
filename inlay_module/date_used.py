
import datetime
now = datetime.date.today()
print(now )
print(datetime.date(2013, 12 ,2))

birthday = datetime.date(1990, 1, 12)
print(now - birthday)


from timeit import Timer
print(Timer('t=a; a=b; b=t;', 'a=1; b=2').timeit())
print(Timer('a,b = b,a', 'a=1; b=2').timeit())


def average(values):
    """Computes the arithmetic mean of a list of numbers.

    >>> print(average([20, 30, 70]))
    40.0
    """
    return sum(values) / len(values)
import doctest
doctest.testmod()


print("-----------------------------------------")


def getYesterday():
    today = datetime.date.today()
    oneday = datetime.timedelta(days = 1)
    yesterday = today - oneday
    return yesterday
print(getYesterday())
