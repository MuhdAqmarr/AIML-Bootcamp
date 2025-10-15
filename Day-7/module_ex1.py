import math
import inspect

# num=int(input("Enter a number to find the square root: "))
# print(f'Square root of {num} is', round(math.sqrt(num), 2))

functions=inspect.getmembers(math, inspect.isbuiltin)
print("All function in math module: ")
for n, func in functions:
    print(n, end=', ')
# or
# for func in functions:
#     print(func[0], end=', ')