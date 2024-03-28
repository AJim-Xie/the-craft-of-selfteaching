from IPython.core.interactiveshell import InteractiveShell
# InteractiveShell.ast_node_interactivity = "all"
import random
'''
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

#可变有序容器List列表；不可变(当前已有部分不可变，可以增加元素)有序容器tuple元组
L3=L1.copy()
L1.insert(0,12)
print(L1,L3,sep='\n')
L1.reverse()
print(L1)
L1.pop(-1)   #pop --> index
L1.remove(2)  #remove-->value
L3.clear()
print(L3,L1,sep='~~~')


t1 = (2,)
t2 = (2)
t3 = 2,
print(type(t1),type(t2),type(t3),sep='~~~')
print(t1==t3)

s2 = set()
d1 = {}
print(s2,type(s2),d1,type(d1),sep='~~')
'''
admins = {'Moose', 'Joker', 'Joker'}
moderators = {'Ann', 'Chris', 'Jane', 'Moose', 'Zero'}

print(f'并集{admins|moderators}')
print(f'交集{admins&moderators}')
print(f'差集1{admins-moderators}')
print(f'差集{moderators-admins}')
print(f'对称差集{admins^moderators}')
print(f'admins的长度{len(admins)}',f'{max(admins)}',f'{min(moderators)}',sep='~~~')

tester ={'Joker','Moose','Moose'}
ter = {'Moose'}
print(f'tester != admins：{tester!=admins}')
print(f'admins is subset of tester:{admins.issubset(tester)}')
print(f'tester < admins :{tester<admins}')
print(f'admins is superset of ter :{admins.issuperset(ter)}')

ter.discard('Joker')
print(ter)
# ter.discard('Moose')
# print(ter)
ter.intersection_update({'a','Moose'})
ter.difference_update({'a','b','c',})
print(f'ter = {ter}')