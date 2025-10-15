print('Dictionary in Python')
our_dictionary=[
    {'id':1, 'name':'John', 'age':25},
    {'id':2, 'name':'Anna', 'age':22},
    {'id':3, 'name':'Mike', 'age':32},
    {'id':4, 'name':'Sara', 'age':28}
]

for person in our_dictionary:
    print(f"ID: {person['id']}, Name: {person['name']}, Age: {person['age']}")

for person in our_dictionary:
    print("ID:", person['id'], "Name:", person['name'], "Age:", person['age'])