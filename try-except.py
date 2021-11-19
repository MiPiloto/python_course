def add_calculator():
    print("Enter two numbers to add:")
    num1 = input("Type first number: ")
    num2 = input("Type second number: ")
    
    try:
        answer = int(num1) + int(num2)
    except ValueError: 
        print("\nWe can only add two NUMBERS, so you can't type any letter, OK?")
        print("Try again: \n")
        add_calculator()
    else:
        print("Your sum is " + str(answer) + "!")

#add_calculator()

while True:
    print("\nWhen you're tired of this, type 'q' to quit.")
    
    print("Enter two numbers to add:")
    num1 = input("Type first number: ")
    if num1 == 'q': 
        break
    num2 = input("Type second number: ")
    if num2 == 'q': 
        break
    
    try:
        answer = int(num1) + int(num2)
    except ValueError: 
        print("\nWe can only add two NUMBERS, so you can't type any letter, OK?")
        print("Try again: \n")
        add_calculator()
    else:
        print("Your sum is " + str(answer) + "!")
    