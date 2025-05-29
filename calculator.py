num_1 = float(input(" Enter number: "))
num_2 = float(input(" Enter another number: "))
choose_operator = input(" Choose a sign (+, -, %, /, * )")

def calculator_app():
    if choose_operator == '+':
        return num_1 + num_2
    elif choose_operator == '-':
        return num_1 - num_2
    elif choose_operator == '%':
        return num_1 % num_2
    elif choose_operator == '*':
        return num_1 * num_2
    elif choose_operator == '/':
        if num_2 != 0:
            return num_1 / num_2
        else:
            return "Error: Division by zero!"
    else:
        return "Invalid operator"
result = calculator_app()
print("Result", result)