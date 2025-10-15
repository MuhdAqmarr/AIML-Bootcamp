# try:
#     num1=float(input("Enter first number: "))
#     num2=float(input("Enter second number: "))
#     sum=num1+num2
#     print("The sum is:",sum)
# except Exception as e:
#     print('Error:',e)
# finally:
#     print("Execution completed.")

try:
    num1=float(input("Enter first number: "))
    num2=float(input("Enter second number: "))
    div=num1/num2
    print("The division is:",div)
except Exception as e:
    print('Error:',e)
finally:
    print("Execution completed.")
