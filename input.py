car = input("What car do you like the most? ")
print(car.title() + " is a very good car!")

seats = input("How many seats do you need? ")
seats = int(seats)
if seats > 8:
    print("You will have to wait for a free table, I'm sorry!")
else:
    print("Your table is ready!")

num = input("Enter a number to check if it is divisible for 10: ")
num = int(num)
if num % 10 == 0:
    print(num + " is divisible for ten!")
else:
    print("This number is not divisible for ten.")