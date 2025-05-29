name = input(" Enter your name ")

school = input(" Enter your school name ")
print("You attend ", school)

# function that calculate age

from datetime import datetime


def calculate_age_in_month(birth_year,birth_month,birth_day):
    today = datetime.today()
    birth_date = datetime(birth_year,birth_month,birth_day)
    age = today.year-birth_date.year-((today.month,today.day) < (birth_date.month,birth_date.day))
    return age

birth_year = int(input("Enter your birth year: "))
birth_month  = int(input("Enter your birth month (1-12): "))
birth_day = int(input("Enter your birth day(1-31): "))

age = calculate_age_in_month(birth_year,birth_month,birth_day)

print(f"Your age is: {age} years old ")