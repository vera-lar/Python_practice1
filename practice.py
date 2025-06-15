def get_grades(scores):
    if scores in range(90, 100):
        print("A")
    elif scores in range(70, 89):
        print('B')
    elif scores in range(50, 69):
        print('C')
    elif scores < 50:
        print('F')


    else:
        print("Invalid input")

