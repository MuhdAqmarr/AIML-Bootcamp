# Simple calculator functions
def add(num1, num2):
    return num1 + num2

def multiply(num1, num2):
    return num1 * num2

def avg(num1, num2):
    return (num1 + num2) / 2

def subtract(num1, num2):
    return num1 - num2

def divide(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Error! Division by zero."



#program to use the functions
print("Welcome to the Calculator Program!\n")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
while True:
    print("\nSelect operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Average")
    print("6. Exit")

    op_input = input("Enter choice (1/2/3/4/5/6): ")
    # If the user types any alphabetic character, exit the program immediately
    if any(ch.isalpha() for ch in op_input):
        print("Alphabetic character detected. Exiting the program. Goodbye!")
        break

    # Try to parse numeric choice; handle non-numeric input gracefully
    try:
        op = int(op_input)
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 6.")
        continue

    if (op == 6):
        print("Exiting the program. Goodbye!")
        break
    if (op < 1 or op > 6):
        print("Invalid input. Please enter a number between 1 and 6.")
    else:
        if (op == 1):
            print(f"The sum of {num1} and {num2} is: {add(num1, num2)}")
        elif (op == 2):
            print(f"The difference between {num1} and {num2} is: {subtract(num1, num2)}")
        elif (op == 3):
            print(f"The product of {num1} and {num2} is: {multiply(num1, num2)}")
        elif (op == 4):
            print(f"The quotient of {num1} divided by {num2} is: {divide(num1, num2)}")
        elif (op == 5):
            print(f"The average of {num1} and {num2} is: {avg(num1, num2)}")
    

    # if op in [1, 2, 3, 4, 5]:
    #     num1 = int(input("Enter first number: "))
    #     num2 = int(input("Enter second number: "))

    #     if op == 1:
    #         print(f"The sum of {num1} and {num2} is: {add(num1, num2)}")
    #     elif op == 2:
    #         print(f"The difference between {num1} and {num2} is: {subtract(num1, num2)}")
    #     elif op == 3:
    #         print(f"The product of {num1} and {num2} is: {multiply(num1, num2)}")
    #     elif op == 4:
    #         print(f"The quotient of {num1} divided by {num2} is: {divide(num1, num2)}")
    #     elif op == 5:
    #         print(f"The average of {num1} and {num2} is: {avg(num1, num2)}")
    # elif op == 6:
    #     print("Exiting the program. Goodbye!")
    #     break
    # else:
    #     print("Invalid input. Please enter a number between 1 and 6.")


