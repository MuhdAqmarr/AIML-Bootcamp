from ourpack import calc
while True:
    try:
        fnum=float(input('Enter first number: '))
        snum=float(input('Enter Second Number: '))
        op=input('Choose operation +,-,*,/: \t')
        if(op=='+'):
            print('Result: \t',calc.add(fnum,snum))
        elif(op=='-'): 
            print('Result: \t',calc.sub(fnum,snum))
        elif(op=='*'): 
            print('Result: \t',calc.multi(fnum,snum)) 
        elif(op=='/'): 
            print('Result: \t',calc.div(fnum,snum))         
        else:
            raise ValueError
        
    except ZeroDivisionError as ze:
        print('Divison by 0 not allowed',ze)
    except ValueError as ve:
        print('Error in values',ve)
    except Exception as ex:
        print('Error!!!',ex) 
    choice=input('Do you wanna contiue? if yes press y: \t').lower()
    if(choice!='y'):
        print('Bye')
        break