import time

import sys
from sys import argv,path
'''print(time.strftime('%Y-%M-%D %H:%M:%S',time.localtime(time.time())))

file = open('C:\\sers\\www\\Desktop\\a.txt', 'r+')
for i in range(20000000):
    i = str(i)
    file.write(i)
    file.write('\r\n')
print(time.strftime('%Y-%M-%D %H:%M:%S',time.localtime(time.time())))'''






str_i = 'werqwerqwe'
str_1 = str_i[-1:] #步长为负数时，列表切割方向也会改变
str_2 = str_i[1:-1:2]
print(str_1)
print('这是：'+str_2)

print(len(str_1))
print(len(str_1))



print(str_1*5,end=' ')


x='runoob';sys.stdout.write(x +'\n')




# def path():
#     print('1')
#     return '1'
print('path:', path)
print(sys.argv)

print(isinstance(str_1,int))

def reverseword(input):
    inputwords = input.split(" ")
    inputwords = inputwords[-1::-1] #调换列表顺序
    outputwords = ' '.join(inputwords)
    print(outputwords)
    return outputwords


if __name__ == '__main__':
    reverseword('i like rr')

