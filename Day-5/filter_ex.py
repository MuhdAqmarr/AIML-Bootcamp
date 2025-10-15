students_marks={
    'Sam':60,
    'Raj': 55,
    'Mihir':35,
    'Sandy' :45,
    'Niraj': 76,
    'Deep' :40,
    'Garima': 54
    }

print('All Students')
for k,v in students_marks.items():
    print(f'Name: {k}, Marks:{v}')
pass_students=dict(filter(lambda i:i[1]>=50, students_marks.items()))
print('\nPassed Student')
for k,v in pass_students.items():
    print(f'Name: {k}, Marks:{v}')

#ascending order
sort_pass_student=dict(sorted(pass_students.items(), key=lambda i:i[1]))
print('\nAscending order')
for k,v in sort_pass_student.items():
    print(f'Name: {k}, Marks: {v}')

#descending order
sort_pass_student=dict(sorted(pass_students.items(), key=lambda i:i[1], reverse=True))
print('\nDescending order')
for k,v in sort_pass_student.items():
    print(f'Name: {k}, Marks: {v}')