#!/usr/bin/python3


class A:
    pass


class B(A):
    pass


print(isinstance(A(), A))
print(type(A()) == A)
print(isinstance(B(), A))
print(type(B()) == A)


var1 = 10
var2 = 1
print(var1)
print(var2)

del var1, var2
# print(var1)


str1 = "substring"
print(str1)
print(str1[0: -1])
print(str1[0: 11])
print(str1[2:])
print(str1[2: 3])
print(str1 * 2)
print(str1 + "test")

print("ru\naaa")
print(r"ru\n11fdsa")

print("""
fasfdasfasdfdasfasdfafdas
fasdfsda
fasdfsad
fasd
""")

print(
    '''
    fafasfdsa \
    fdasdfsa \
    fasdf\
    aaffsda\
    '''
)


word = 'python'
print(word[0], word[1])
print(word[-1], word[-6])

print("---------------------- list -------------------------")
list1 = ['abcd', 3433, 2.343, 'runoob', 20.4]
tinyList = [123, 'runoob']
print(list1)
print(list1[0])
print(list1[0: 3])
print(list1[2:])
print(tinyList * 2)
print(list1 + tinyList)

print("---------------------- list change ---------------------")
a = [1, 2, 3, 4, 5, 6, 7]
a[0] = 9
a[2: 5] = [13, 14, 15]
print(a)
a[2: 5] = []
print(a)

print("------------------------- tuple -----------------------")
tupleS = ('abcd', 888, 2.343, 'runnot', 2234)
tinyTuple = (134, 'runoob')
print(tupleS)
print(tupleS[0])
print(tupleS[1: 3])
print(tupleS[2:])
print(tinyTuple * 2)
print(tupleS + tinyTuple)

tup1 = ()
tup2 = (20,)
print(tup2)


