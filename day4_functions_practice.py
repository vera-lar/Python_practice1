grade_students = [85, 45, 33, 55, 92, 41]

for grade in grade_students:
    if grade >= 50:
        print(f"{grade} - pass")
    else:
        print(f"{grade} - fail")



   #even_or_old function 
def even_or_odd(seq):
    for num in seq:
        if num % 2 == 0:
            print(f"{num} is even")
        else:
            print(f"{num} is odd")

# ✅ Example usage:
even_or_odd([7, 8, 4, 5, 9, 4])


       #lambda function 


multiply3 = lambda a: a * 3
print(multiply3(3))



#list comprehension

filter_pass_students = {"mary": 45, "burke": 65, "eleanor": 36, "esther": 77}

for name, grade in filter_pass_students.items():
    if grade >= 50:
        print(f"{name} - pass")
    else:
        print(f"{name} - fail")
