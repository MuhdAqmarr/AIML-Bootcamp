# username=str(input("Enter your username: "))
# age=int(input("Enter your age: "))
# salary=float(input("Enter your salary: "))
# isGraduate=bool(input("Are you a graduate? (True/False): "))
# stayStatus=str(input("Enter your stay status: "))

# print("welcome Mr.\\Ms. ", username)
# print("Your age is ", age)
# print("Your salary is ", salary)
# print("Are you a graduate?: ", isGraduate)
# print("Your stay status is", stayStatus)

# Adding Two Numbers
# num1=int(input("Enter first number: "))
# num2=int(input("Enter second number: "))
# sum=num1+num2
# print(f"The sum of {num1} and {num2} is: ", sum)

# Multiply Two Numbers
# num1=int(input("Enter first number: "))
# num2=int(input("Enter second number: "))
# product=num1*num2
# print(f"The product of {num1} and {num2} is: ", product)

# Division Two Numbers
# num1=int(input("Enter first number: "))
# num2=int(input("Enter second number: "))
# product=num1/num2
# print(f"The division of {num1} by {num2} is: ", product)

# Remainder Two Numbers
# num1=int(input("Enter first number: "))
# num2=int(input("Enter second number: "))
# product=num1%num2
# print(f"The remainder of {num1} by {num2} is: ", product)

# Taking more than one input using single line
num1, num2 = map(int, input("Enter two numbers separated by space: ").split())
sum = num1 + num2
print(f"The sum of {num1} and {num2} is: ", sum)
print(f"Number entered {num1} and {num2}")