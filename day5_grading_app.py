def get_grade(score):
    if 90 <= score <= 100:
        return 'A'
    elif 70 <= score <= 89:
        return 'B'
    elif 50 <= score <= 69:
        return 'C'
    elif 0 <= score < 50:
        return 'F'
    else:
        return 'Invalid'

students = []
user_choice = 0

while user_choice < 3:
    try:
        user_input = input(f"Enter name and score of student {user_choice + 1} (e.g., John 85): ")
        name, score = user_input.split()
        score = int(score)
        grade = get_grade(score)
        
        if grade == 'Invalid':
            print("Score is invalid. Please enter a number between 0 and 100.")
            continue

        students.append({'name': name.capitalize(), 'score': score, 'grade': grade})
        user_choice += 1
    except ValueError:
        print("Invalid input format. Please enter in 'Name Score' format.")

# Compute class stats
scores = [student['score'] for student in students]
average = sum(scores) / len(scores)
highest = max(students, key=lambda x: x['score'])
lowest = min(students, key=lambda x: x['score'])

# Print report
print("\nClass Report")
print("============")
for student in students:
    print(f"{student['name']} scored {student['score']} and got grade {student['grade']}")

print(f"\nClass average score: {average:.2f}")
print(f"Highest scorer: {highest['name']} with {highest['score']}")
print(f"Lowest scorer: {lowest['name']} with {lowest['score']}")
