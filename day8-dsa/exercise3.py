secret_numbers = [30, 22, 50, 90, 77]

while True:
    try:
        user_input = input("Enter your number, let's check: ").strip()
        user_number = float(user_input)

        if int(user_number) in secret_numbers:
            print(f"Yes! Found it: {int(user_number)}")
            break
        else:
            print(f"{user_number} not found.")
    except ValueError:
        print("INVALID INPUT. Please enter a valid number.")

print(f"WOW! You found the number {int(user_number)} among the numbers.")
