glossary = {
    "python":"an easy and powerful language!",
    "unity":"good for games!",
    "java":"old and reliable language.",
    "ruby":"useful for mobile development!",
    "javascript/React":"fabulous language and framework, in high ascension!",
    "swift":"used in IOS development!",
}

print("Here are some famous and useful languages for programming.\n")

for keys,values in glossary.items():
    print("We have " + keys.title() + ": " + glossary[keys].title() + "\n")


rivers={
    "brasil":"amazonas",
    "egito":"nilo",
    "eua":"mississipi",
}

for key,value in rivers.items():
    print("The river " + value + " crosses this country: " + key.title())

for river in rivers.values():
    print(river.title())

for country in rivers.keys():
    print(country.title())

persons = ["bruce","john","jack","jill","claire"]
favorite_languages = {"bruce":"java","homer":"python","jill":"ruby","kim":"c"}

for person in favorite_languages.keys():
    if person not in persons:
        print(person.title() + ", Please choose your favorite language!")
    else:
        print(person.title() + ", thank you for your submission, enjoy learning " + favorite_languages[person].title() + "!")


dog = {
    "owner":"bruce",
    "race":"doberman"
}

cat = {
    "owner":"witch",
    "race":"black and spooky"
}

fisch = {
    "owner":"nemo",
    "race":"clown-fish"
}

bird = {
    "owner":"clock",
    "race":"cuco"
}

pets = [dog,cat,fisch,bird]

for pet in pets:
    if pet == cat:
        print("Take your torches, here is " + pet["owner"].title() + "'s " + pet["race"] + " cat!")
    else:
        print("Welcome, " + pet["owner"].title() + " and " + pet["race"].title() + "!" )


favorite_places = {
    "bruce":{"first":"cave","second":"mansion","trird":"rooftops"},
    "clark":{"first":"krypton","second":"daily-bugle","trird":"phone-cabin"},
    "peter":{"first":"skyscrapper","second":"may's house","trird":"laboratory"},
}


for hero,place in favorite_places.items():
    print("\n" + hero.title() + " likes these places: ")
    places = str(place["first"].title() + ", " + str(place["second"].title()) + ", and " + str(place["trird"].title()))
    print("Favorite places are: " + places)

cities = {
    "brazil":["sp","mg","rj"],
    "germany":["bl","col","bav"],
    "japan":["tk","ok","shj"],

}

for city,states in cities.items():
    print(city.title() + " has these states: " + str(states))