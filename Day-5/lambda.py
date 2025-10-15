# def add(a,b):
#     total= a+b
#     return total

# result=add(12,15)
# print(result)

# addition = lambda a, b: a + b
# multi=lambda a,b:a*b
# div=lambda a,b:a/b
# avg=lambda a,b:(a+b)/2
# sub=lambda a,b:(a-b)

# num1=int(input('Enter first Number:\t'))
# num2=int(input('Enter Second Number: \t'))

# print('Multiplication result: ',multi(num1,num2))
# print('Sutraction result: ',sub(num1,num2))

#lambda example to find out odd or even number

check_odd= lambda n:"Odd Number" if n%2==1 else 'Even Number'
num1=int(input('Enter Number to check Odd or Even: \t'))
print(check_odd(num1))