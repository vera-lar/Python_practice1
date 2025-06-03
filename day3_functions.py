def greet_user(name):
    print("Hello "+ name )


greet_user("vera")

#A simple calculator app inside the greet function

def calculate_area(length, width):
        print("The length and width of a rectangle is : " , length + width)
calculate_area(4, 4)

# function to check even and odd

def is_even(num):
      if num % 2 == 0:
            print("it's an even number ")

      elif num % 2 != 0:
            print("it's  an odd number ")     
      else:
            print("it's not a number ")

is_even(5)

# function that sum all the given number 

def sum_all(*args):
      print(sum(args))

sum_all(3, 49)

# function for student grade

def student_grade(name, score):
    if score >= 50 :
       print( "Pass")
    elif score <= 50:
          print( "Fail")
    else:
          print("You have no score")
    
student_grade("Burke", 53)
  