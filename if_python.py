food = "carne"

print("Is food == 'carne'? I predict true. " + str(food == "carne"))
print("Is food == 'arroz'? I predict false. " + str(food == "arroz"))

print("Is food == 'Carne'? I predict true. " + str(food.lower() == "carne"))
print("Is food == 'carne'? I predict true. " + str(food != "carne"))

numbers = [1,2,3,4,5]

print("Comparing numbers of array: " + str(numbers[0] == numbers[1]))
print("Comparing numbers of array: " + str(numbers[0] != numbers[1]))

print("Both conditions should be true: " + str(numbers[0] == numbers[1] and numbers[2] == numbers[3]))
print("Both conditions should be true: " + str(numbers[0] != numbers[1] and numbers[2] != numbers[3]))
print("Both conditions should be true: " + str(numbers[0] != numbers[1] or numbers[2] == numbers[3]))
print("Both conditions should be true: " + str(numbers[0] == numbers[1] or numbers[2] == numbers[3]))

if numbers[0] != numbers[3]: print("Not Equal!")

print("is 2 there? " + str(2 in numbers))
if 2 in numbers: print("2 is there!")
print("is 6 there? " + str(6 in numbers))
if 6 not in numbers: print("6 is not there!")




