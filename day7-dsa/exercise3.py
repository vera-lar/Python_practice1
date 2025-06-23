names_of_student = []

while len(names_of_student) < 5:
    name = input("Enter student name  ").lower()
    names_of_student.append(name)
names_of_student.sort()
print("sorted student names :")
for i in names_of_student:
    print(f"{i} ")
        