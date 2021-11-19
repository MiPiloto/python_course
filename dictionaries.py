person1 = {
    "first_name":"mi",
    "last_name":"pi",
    "age":33,
    "city":"são carlos",
    }

person2 = {
    "first_name":"jaque",
    "last_name":"furu",
    "age":31,
    "city":"praia grande",
}

person3 = {
    "first_name":"piloto",
    "last_name":"pai",
    "age":63,
    "city":"são carlos",
}

people=[person1,person2,person3]

for person in people:
    print(person)

print(person)

favorite_numbers = {
    "seya":24,
    "shiryu":7,
    "shun":2424,
    "yoga":0.000,
    "ikki":666,
    }

print("Saints' favorite numbers are curious.\nSeya likes " +
    str(favorite_numbers["seya"]) + " and Shiryu chose " +
    str(favorite_numbers["shiryu"]) + ".\n" + 
    "Yoga is absolute cold with his number, " + str(favorite_numbers["yoga"]) +
    ", and Ikki sent his hell number, " + str(favorite_numbers["ikki"]) + 
    ", to Shun when he saw his brother chose " + str(favorite_numbers["shun"]) + ".")


glossary = {
    "python":"easy and powerful language!",
    "unity":"good for games!",
    "java":"old and reliable language.",
    "ruby":"useful for mobile development!",
    "javascript/React":"fabulous language and framework, in high ascension!",
}

print("Here are some famous and useful languages for programming.")
print("First, Python:\n" + glossary["python"].title() + "\n")
print("Second, Unity:\n" + glossary["unity"].title() + "\n")
print("Third is Java:\n" + glossary["java"].title() + "\n")
print("Fourth goes Ruby:\n" + glossary["ruby"].title() + "\n")
print("Fifth and final is Javascript/React:\n" + glossary["javascript/React"].title() + "\n")
