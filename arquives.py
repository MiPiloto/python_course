file_path = "python-course/learning_python.txt"

print("First example:\n") # lendo cada linha
with open(file_path) as file:
    for line in file:
        print(line.rstrip())
print("")

print("Second example:\n") # lendo cada linha e armazenando em outra variável
with open(file_path) as file:
    file_lines = file.readlines()
    text=""
    for line in file_lines:
        text += line
print(text)
print("")

print("Third example:\n") # lendo cada linha e trocando uma palavra por outra
with open(file_path) as file: 
    file_lines = file.readlines()
    text=""
    for line in file_lines:
        text += line.replace("Python","Java")
print(text)

    