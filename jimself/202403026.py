from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

for i in range(1,10):
    fileName= str(i).zfill(4)+('.mp4')
# print(fileName.title().center(60,'-'))

print('你哈'.encode(),ord('e'),chr(122),sep='\n')