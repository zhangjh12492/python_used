#!/usr/bin/python3

# 导入特定成员
from sys import argv,path
import sys; x = 'runoob'; sys.stdout.write(x + '\n')
print("Hello, World!")
print("this is an unicode string")
# input("\n\n按下 enter 键后退出。")

aaa = "bbb"
if aaa == "aaa":
    print("aaa")
elif aaa == "bbb":
    print("bbb")
else:
    print("ccc")

print("no change line", end="")
print(" until")

print("===========Python import mode=================")
print('命令行参数为:')
for i in sys.argv:
    print(i)
print('\npython 路径为', sys.path)
print('\npython 版本为', sys.version)

print("============ python from import ===========================")
print('path:', path)

print(max(111, 333, 444444, 22, 34322343, 23425611, 3243235))

print('---------------------------------------------------')
