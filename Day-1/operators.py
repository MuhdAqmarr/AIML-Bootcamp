# Assignement operators: =, +=, -=
# price=float(input("Enter Product Price: "))
# discount=price*0.10
# disPrice=price-discount
# print(f"Price: {price} \nDiscount: {discount} \nDiscounted Price: {disPrice}")
# print("Discounted Price:", disPrice)

# salary=50000.50
# bonus=5000.60
# print(f"Salary {salary} and Bonus {bonus}")
# salary += bonus
# print("Total Salary with bonus: ", salary) 

# salary=50000.50
# tax=salary*0.10
# print(f"Salary {salary} and Tax {tax}")
# salary -= tax
# print("Total Salary after tax: ", salary) 



# Comparison operators: ==, >, >=, <, != etc.

# age=int(input("Enter your age: "))
# if(age>=18):
#     print("You are eligible to cast your vote")
# else:
#     print("You are not eligible to cast your vote")

# print("end of program")


# marks=int(input("Enter your marks without '%' sign: "))
# if(marks<30):
#     print("You are failed")
# else:
#     print("You are passed")


# accessCode=input("Enter Access Code: ")
# if(accessCode!="wes12"):
#     print("Invalid Access Code")
# else:
#     print("Access Granted")
#     print("Welcome to your course")


# accessCode=input("Enter Access Code: ")
# if(accessCode=="wes12"):
#     print("Access Granted")
# else:
#     print("Invalid Access Code")



# Logical Operators: and, or, not
# phyMarks=int(input("Enter your Physics marks: "))
# chemMarks=int(input("Enter your Chemistry marks: "))
# mathMarks=int(input("Enter your Maths marks: "))
# if(phyMarks>=50 and chemMarks>=55 and mathMarks>=60):
#     print("You are passed")
# else:
#     print("You are failed")


# idProof=input("Enter your ID Proof: ")
# if(idProof=="Passport" or idProof=="Driving License" or idProof=="Voter ID"):
#     print(f"Valid ID {idProof} accepted")
# else:
#     print("Only Passport, Driving License or Voter ID is accepted as ID Proof")
#     print(f"Your ID Proof is {idProof}, which is not valid")


# mathMarks=int(input("Enter your Maths marks: "))
# gapYear=int(input("Enter year Gap if any otherwise enter 0: "))
# if((mathMarks<=55) and (gapYear!=0)):
#     print("You are not eligible for BTech")
# else:
#     print("You are eligible for BTech")

name=input("Enter your name: ")
if(not name):
    print("Name cannot be empty")
else:
    print(f"Your name is {name}")