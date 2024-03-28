from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

#字典是映射容器  Map

class1 = {'name':'Jim','gender':'male','age':10,'Cls':'Math'}
print(f'class1 is {class1},{type(class1)}',f'{class1["gender"]}',sep='~~~')
class1['name']='Joe'
print(f'{class1["name"]}')
print(f'class1 lens is :{len(class1)}',f'min class1 is :{min(class1)}',f'max class1 is {max(class1)}',f'{sorted(class1,reverse=True)}',sep='\n')
# class1.clear()
print('Line1'.center(20,'*'))
for key,value in class1.items():
    print(f'{key},{value}')

print('Line2'.center(20,'*'))
s = class1.popitem()
print(s)

print('Line3'.center(20,'*'))
for i,v in enumerate('Great Wall'):
    print(i,v)