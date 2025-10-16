class InvalidMarks(Exception):
    pass
    
def check_marks(marks):
    if(marks<0):
        raise InvalidMarks('Marks should not be negative')
    elif(marks>50):
        raise InvalidMarks('Marks should be witin range 0-50')
   
    else:
        print(f'Marks {marks} are accepted')
