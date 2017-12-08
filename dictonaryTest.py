#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# coding=utf-8

dict = {}
dict['one'] = '1 - 菜鸟'
dict[2] = '2 - 菜鸟'

tinyDict = {'name': 'jacy', 'code': 1, 'age': 12}
print(dict['one'])
print(dict[2])
print(dict.keys())
print(dict.values())
print(tinyDict)
print(tinyDict.keys())
print(tinyDict.values())


print('---------------------------------------------------')

dict3 = {x: x**2 for x in (2, 4, 6)}
print(dict3)

print('你好 世界')
