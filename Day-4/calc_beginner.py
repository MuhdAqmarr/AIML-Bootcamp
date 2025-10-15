# Simple calculator functions
def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        return 'Error: division by zero'
    return num1 / num2

def average(num1, num2):
    return (num1 + num2) / 2


# Function to input one-line multiple choices like '1 3 5' or '2,4'
def parse_choices(line):
    # replace commas with spaces, then split on whitespace
    line = line.replace(',', ' ')
    parts = line.split()
    choices = []
    for p in parts:
        if p.isdigit():
            n = int(p)
            if n not in choices:
                choices.append(n)
    return choices


# Main program
print('Welcome to the Beginner Calculator')

number1 = int(input('Enter first number: '))
number2 = int(input('Enter second number: '))

while True:
    print('\nChoose operations (you can type several, separated by space or comma):')
    print('1 - Add')
    print('2 - Subtract')
    print('3 - Multiply')
    print('4 - Divide')
    print('5 - Average')
    print('6 - Exit')

    line = input("Enter choice(s) like '1 3 5' or '2,4': ")
    choices = parse_choices(line)

    if not choices:
        print('No valid choices entered. Try again.')
        continue

    if 6 in choices:
        print('Goodbye!')
        break

    for c in choices:
        if c == 1:
            print(f'Add: {number1} + {number2} = {add(number1,number2)}')
        elif c == 2:
            print(f'Subtract: {number1} - {number2} = {subtract(number1,number2)}')
        elif c == 3:
            print(f'Multiply: {number1} * {number2} = {multiply(number1,number2)}')
        elif c == 4:
            print(f'Divide: {number1} / {number2} = {divide(number1,number2)}')
        elif c == 5:
            print(f'Average: ({number1} + {number2})/2 = {average(number1,number2)}')
        else:
            print(f'Ignored invalid choice: {c}')

    again = input('Do you want to enter new numbers? (y/n): ').strip().lower()
    if again in ('y', 'yes'):
        number1 = int(input('Enter first number: '))
        number2 = int(input('Enter second number: '))

print('\nProgram ended.')
