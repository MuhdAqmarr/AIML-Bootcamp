# def factorial(num):
#     if(num==0 or num==1):
#         return 1
#     else:
#         return num * factorial(num-1)

# number = int(input("Enter a number to find its factorial: "))
# print(f"The factorial of {number} is: {factorial(number)}")


#Write a python function which converts inches to cm.
# 1 inch = 2.5cm
# def inches_to_cm(inches):
#     return inches * 2.54

# print("\nConvert inches to cm")
# inch = float(input("Enter length in inches: "))
# print(f"{inch} inches is equal to {inches_to_cm(inch)} cm")

#write a function to findout the table of given number
def print_table(num):
    print(f"\nTable of {num}:")
    for i in range(1, 20):
        print(f"{num} x {i} = {num * i}")
number = int(input("Enter a number to find its table: "))
print_table(number)
