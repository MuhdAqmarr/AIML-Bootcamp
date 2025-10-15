import random

# print("A random number between 1 and 1000 is")
# print(random.randint(1, 1000))
def findwinner():
    name=input("Enter your name: ")
    lucky_number=random.randint(1, 10)
    print(f'Hello {name}, your lucky number is {lucky_number}')
    print("\n")
    if lucky_number==7:
        print("You won a Proton car!")
    elif lucky_number==1:
        print("You won a bicycle!")
    elif lucky_number==9:
        print("You won a laptop!")
    else:
        print("Sorry, you did not win anything. Try again!")