# import os
# # file_path= r'D:\AIML\Day-8\ourfiles\sample.txt'
# file_path= 'D:\\AIML\Day-8\\ourfiles\\sample.txt'

# file=open(file_path,'w')
# content=input('Enter text to write in file')
# file.write(content)
# file.close()

# import os
# # file_path= r'D:\AIML\Day-8\ourfiles\sample.txt'
# filepath= 'D:\\AIML\\Day-8\\ourfiles'
# filename=input('Enter File Name to Create File: \t')
# fullpath=os.path.join(filepath,filename)
# file=open(fullpath,'w')
# content=input('Enter text to write in file')
# file.write(content)
# print(f'File {filename} create at {fullpath} and content saved in file')
# file.close()

import os
# file_path= r'D:\AIML\Day-8\ourfiles\sample.txt'

filepath= os.getcwd()
filename=input('Enter File Name to Create File: \t')
fullpath=os.path.join(filepath,filename)
file=open(fullpath,'w')
content=input('Enter text to write in file')
file.write(content)
print(f'File {filename} create at  {fullpath}  and content saved in file')
file.close()