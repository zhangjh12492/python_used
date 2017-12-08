#!/usr/bin/python3

student = {'tom', 'gude', 'Tom', 'Tom', 'Rose'}
print(student)

# 成员测试
if('Rose' in student):
    print('Rose 在集合中')
else:
    print('Rose 不在集合中')

# set 可以进行集合运算
print('-------------------------------------')
a = set('aaaabc')
b = set('bbbbae')
print(a)
print(b)
print(a - b)    # a和b的差集
print(a | b)    # a和b的并集
print(a & b)    # a和b的交集
print(a ^ b)    # a和b中不同时存在的元素
