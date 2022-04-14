import os

# assing a path to var
actualPath = os.getcwd()

# look at the all path directories
print("Directories:",os.listdir(actualPath))

# create a new join path
newPath = os.path.join(actualPath,'test')
print("new str Path:",newPath)

# create directories into the folder
print('FOLDER CREATED SUCCESSFULLY')
os.getcwd(os.mkdir('dataset2'))

# create folder into folder
os.makedirs(os.path.join('dataset','scripts'))

# rename files
os.rename('dataset2', 'datarenamed')

for file in os.listdir():
    if file.endswith('.csv'):
        os.rename(file, f'2021_{file}')


# directorie exists
print('file exist: ', os.path.exists('dataset'))


# metadata
print('absolute path: ',os.path.abspath('prueba'))
print('path size: ',os.path.getsize('prueba'))
print('file changed time: ',os.path.getctime('dataset'))
print('file modification time: ',os.path.getmtime('dataset'))
print('file access time: ',os.path.getatime('dataset'))


# open files
f = open('prueba/hola.txt')

for line in f:
    print(line)

f.close