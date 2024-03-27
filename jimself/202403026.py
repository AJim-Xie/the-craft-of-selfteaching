from IPython.core.interactiveshell import InteractiveShell
# InteractiveShell.ast_node_interactivity = "all"
import random

# for i in range(1,10):
#     fileName= str(i).zfill(4)+('.mp4')
# print(fileName.title().center(60,'-'))

# print('你哈'.encode(),ord('e'),chr(122),sep='\n')

# age=18
# print('AJim\'s age is {}'.format(age))
# print(f'AJim\'s age is {age}')

L1 = [a**2 for a in (1,4,6,7) if a % 2 !=0]
L1.sort()
print(L1)
L1.sort(reverse=True)
print(L1)

L2 = [chr(random.randrange(1000,1012)) for i in range(10) ]
print(L2)

#可变有序容器List列表；不可变有序容器tuple元组
L3=L1.copy()
L1.insert(0,12)
print(L1,L3,sep='\n')
L1.reverse()
print(L1)
L1.pop(-1)   #pop --> index
L1.remove(2)  #remove-->value
L3.clear()
print(L3,L1,sep='~~~')


