try:
    fnum=float(input('Enter first number: '))
    snum=float(input('Enter Second Number: '))
    result=fnum/snum
    print(f'Result:{round(result,4)} after dividing {fnum} by {snum}')
except Exception as e:
    print('Error',e)
finally: 
    print('Good Bye')