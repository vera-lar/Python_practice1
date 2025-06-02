guess_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

while True:
    user_guess_num = int(input("Guess a number: "))
    
    if user_guess_num in guess_nums:
        print("Great! You are right, the number is " + str(user_guess_num))
        break
    else:
        print("Oh no, you missed it!")
        print("No worries! You can try again.")


# odd add even checker 

def check_even_or_odd():
    try:
        user_choiece  = int(input("Enter a number: "))
        if user_choiece  % 2 == 0:
            print(f"{user_choiece } is even.")
        else:
            print(f"{user_choiece } is odd.")
    except ValueError:
        print("Invalid input! Please enter a valid integer.")
check_even_or_odd()       



#Loop practice 
for number in range(1, 21):  # Loop from 1 to 20 (21 is not included)
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")  # Both 3 and 5
    elif number % 3 == 0:
        print("Fizz")      # Only 3
    elif number % 5 == 0:
        print("Buzz")      # Only 5
    else:
        print(number)      # Not a multiple of 3 or 5
