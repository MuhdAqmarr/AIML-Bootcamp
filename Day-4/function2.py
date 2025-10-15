#Default parameter in functions

def info(id, name, city="KL"):
    print(f"Details as follow: \n ID: {id} Name: {name} City: {city}")

info(1, "Alice", "Penang")
info(2, "Bob")
info(3, "Charlie", "Johor")

#we want to create a single method that can able to add 2 numbers, 3 numbers, 4 numbers or 5 numbers and return correct total
def add(num1, num2, num3=0, num4=0, num5=0):
    return num1 + num2 + num3 + num4 + num5
print(f"result: {add(10, 20)}")
print(f"result: {add(10, 20, 30)}")
print(f"result: {add(10, 20, 30, 40)}")
print(f"result: {add(10, 20, 30, 40, 50)}")


def add_numbers(*num):
    return sum(num)
print(f"result: {add_numbers(10, 20)}")
print(f"result: {add_numbers(10, 20, 30)}")
print(f"result: {add_numbers(10, 20, 30, 40)}")
print(f"result: {add_numbers(10, 20, 30, 40, 50)}")
print(f"result: {add_numbers(10, 20, 30, 40, 50, 60, 70, 80, 90, 100)}")

