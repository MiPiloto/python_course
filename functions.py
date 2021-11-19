def display_message():
    print("I'm learning python functions!")

display_message()

def favorite_book(title):
    print("One of my favorite books is " + title.title() + "!")

favorite_book("lord of the rings")

def make_shirt(size="G",text="I love Python"):
    print("Your shirt will be size " + size.title() + " and will have the text " + text.upper() + "!")

make_shirt("m","woohaaaaa")
make_shirt()
make_shirt("m")
make_shirt(text="I love functions!")

def describe_city(name,country="Germany"):
    print(name.title() + " is located in " + country.title())

describe_city("berlim")
describe_city("rome","italy")
describe_city(country="portugal",name="lisboa")

def city_country(city,country):
    full_adress = (city.title() + " is located in " + country.title())
    return full_adress

brazil = city_country("araras","brazil")
print(brazil)
japan = city_country("tokyo","japan")
print(japan)

def make_album(artist,album):
    full_album = {"artist":artist,"album":album}
    return full_album

iron = make_album("iron maiden","senjustu")
print(iron)
metallica = make_album("mettalica","black album")
print(metallica)

def make_album(artist,album,tracks=''):
    if tracks: full_album = {"artist":artist,"album":album,"tracks":tracks}
    else: full_album = {"artist":artist,"album":album}
    return full_album

iron2 = make_album("iron maiden","senjustu",10)
print(iron2)
acdc = make_album("ACDC","Witch'spell")
print(acdc)

while True:
    prompt = print("Let's make an album!  Type 'q' to quit." )
    art = input("Choose an artist: ") 
    if art == "q": break
    alb = input("Choose an album: ")
    if alb == "q": break
    full = make_album(art,alb)
    print(full)
