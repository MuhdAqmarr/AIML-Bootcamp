#print('Write a function to calculate the cube of given number')
#5: 5*5*5=125
# def cube(num):
#     return num ** 3
# number = int(input("Enter a number to find its cube: "))
# print(f"The cube of {number} is: {cube(number)}")


#write a function to calculate bonus of given salary
#function take salary as input and return bonus 10% of salary
def calculate_bonus(salary):
    return salary * 0.10
print("\nCalculate bonus of given salary")
sal = float(input("Enter your salary: RM"))
print(f'Your bonus is: RM{calculate_bonus(sal)}')