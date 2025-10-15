# def function_name(parameters):
#     # Docstring
#     statement(s)


#function without parameters and without return value
# def welcome():
#     print("Welcome to the function example!")
#     print("Our first function in Python.")

# welcome()

# def welcome(name):
#     print(f"Welcome to the function example, Mr./Ms {name}!")

# username = input("Enter your name: ")
# welcome(username)



#function with parameters and with return value
# def add(num1, num2):
#     return num1 + num2

# number1 = int(input("Enter first number: "))
# number2 = int(input("Enter second number: "))
# print(f"The sum of {number1} and {number2} is: {add(number1, number2)}")

def multiply(num1, num2):
    return num1 * num2

number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
print(f"The product of {number1} and {number2} is: {multiply(number1, number2)}")