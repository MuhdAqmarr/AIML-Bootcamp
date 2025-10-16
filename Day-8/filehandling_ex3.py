import os
# file_path= r'D:\AIML\Day-8\ourfiles\sample.txt'
filepath= os.getcwd()
filename=input('Enter File Name to read File: \t')
fullpath=os.path.join(filepath,filename)
if(os.path.exists(fullpath)):
    file=open(fullpath,'r')
    content=file.read()
    print('File Content as follows')
    print(content)
    file.close()
else:
    print(f'No such file {filename} exist')    