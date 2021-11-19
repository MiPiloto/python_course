
while True:
    with open('python-course/guests.txt', 'a') as file:
        name = input("What's your name?\nType 'q' to quit. ")
        if name == 'q':
            break
        file.write(name.title() + "\n")
print(file)

while True:
    with open('python-course/enquete.txt','a') as file:
        question = input("What language do you like programmin with? ")
        if 'python' not in question:
            print("Why not Python?\n")       
            if "java" in question:
                print("Oh Nooooo!")
                break
            elif "ruby" in question:
                print("Why ruby?")
                break
        else:
            file.writelines(question.title() + "\n")
print(file)
