import os as o

# current working directory
currentDirectory = o.getcwd()
print('the current working directory is', currentDirectory)

# making a new directory
o.mkdir('sampledirectory')

import time as t

t.sleep(15)
o.rename('sampledirectory', 'directory')

t.sleep(15)
o.rmdir('directory')
