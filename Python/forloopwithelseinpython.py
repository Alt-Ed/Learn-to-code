# program to display student's marks from record
student_n = 'Soyuj'

marks = {'James': 90, 'Jules': 55, 'Arthur': 77}

for student in marks:
    if student == student_n:
        print(marks[student])
        break
else:
    print('No entry with that name found.')