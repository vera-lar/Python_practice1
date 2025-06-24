total_sum = 0

for i in range(5):
    while True:
       try:
            num = float(input("Enter number {i + 1}"))
            total_sum += num
            break
       except ValueError:
           print("Invalid input. please enter a number. ")
print(f"The sum of the number is {total_sum}")
         
            
