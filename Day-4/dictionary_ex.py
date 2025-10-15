employee = {
    "id": 1,
    "name": "Alice Smith",
    "salary": 55000.50,
}

# print(employee)

# print(f"\nEmployee ID: {employee['id']}")
# print(f"Employee Name: {employee['name']}")
# print(f"Employee Salary: {employee['salary']}")

# print("\nEmployee Details:")
# for key, value in employee.items():
#     print(f"{key}: {value}")

# # Adding key in dictionary
# employee["city"] = "New York"
# print("\nAfter adding city:")
# for key, value in employee.items():
#     print(f"{key}: {value}")

# del employee["salary"]
# print("\nAfter deleting salary:")
# for key, value in employee.items():
#     print(f"{key}: {value}")

print("All keys from Employee dictionary:")
for key in employee.keys():
    print(key, end=" ")

print("\nAll values from Employee dictionary:")
for value in employee.values():
    print(value, end=" ") 

print(employee)
