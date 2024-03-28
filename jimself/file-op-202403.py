from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

import os

f = open('D://1.txt','w')
print(f'{f.name}')   #注意不是f.name()  属性，而不是method

f.close

print('It\'s a Line!'.center(60,'*'))

dir1= 'D://2.txt'

list3= ['\n1','2','\n4']
with open(dir1,'w') as f1:
    print(f'{f1.name}')
    f1.write('Hello\nhello')
    f1.writelines(list3)

with open(dir1,'r') as f1:
    # print(f1.readline())
    # print(f1.readline())
    print(f1.read())

if os.path.exists(dir1):
    os.remove(dir1)
    print(f'{dir1} deleted.')
else:
    print(f'{dir1} does not exist.')

print('It\'s a Line2!'.center(60,'*'))

def sum_of_word(word):
    sum = 0
    for char in word:
        sum += ord(char)-96
    return sum
sum1= sum_of_word('attitude')
print(sum1)