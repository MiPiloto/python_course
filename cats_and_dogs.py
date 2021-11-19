with open('python-course/cats.txt','w') as cats:
    cats.write("Black, Moon and Sir Neko ")

with open('python-course/dogs.txt','w') as dogs:
    dogs.write("Panda, Thor and Maia ")


def open_text(file):
    try:
        with open(file) as file:
            f = file.read()
    except FileNotFoundError: print("File not found.")
    else:
        print(f)

open_text('python-course/cats.txt')
open_text('dogs.txt')

def count_words(file):
    try:
        with open(file) as file:
            f = file.read()
    except FileNotFoundError: print("File not found.")
    else:
        count = f.lower().count("the")
        print(count)

count_words('python-course/test.txt')
