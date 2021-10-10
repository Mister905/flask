# Destructuring variables

student_attendance = { "Tim": 90, "Joe": 80, "Tina": 75 }

print(list(student_attendance.items()))

for student, attendance in student_attendance.items():
    print(f"{student}: {attendance}")
    

# If you don't care about a variable
person = ("Bob", 42, "Mechanic")

name, _, profession = person

print(name, profession)


# If you just want the first variable in a list

head, *tail = [1,2,3,4,5]
print(head)
print(tail)