#Take user marks from user with in 0 to 50
#if user enter outside [0-50] raise Error InvlidMarks using Custom Exception
#Give chance to the user till , he/she entered valid marks
# class InvalidMarks(Exception):
#     pass
    
# def check_marks(marks):
#     if(marks<0):
#         raise InvalidMarks('Marks should not be negative')
#     elif(marks>50):
#         raise InvalidMarks('Marks should be witin range 0-50')
   
#     else:
#         print(f'Marks {marks} are accepted')

# while True:
#     try:   
#         usermarks=int(input('Enter your Marks[0-50]: ') )
#         check_marks(usermarks) 
#     except InvalidMarks as e:
#         print('Invalid Marks : ',e)    
#     except Exception as ex:
#         print('Error !!!',ex) 
#     else:
#         print('Recorded') 
#         break
#     choice=input('Do you wanna re-enter marks? if yes press y To exit press any other key: \t').lower()
#     if(choice!='y'):
#         print('Bye')
#         break  

from ourpack import mark

while True:
    try:   
        usermarks=int(input('Enter your Marks[0-50]: ') )
        mark.check_marks(usermarks) 
    except mark.InvalidMarks as e:
        print('Invalid Marks : ',e)    
    except Exception as ex:
        print('Error !!!',ex) 
    else:
        print('Recorded') 
        break
    choice=input('Do you wanna re-enter marks? if yes press y To exit press any other key: \t').lower()
    if(choice!='y'):
        print('Bye')
        break  