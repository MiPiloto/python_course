def cities(city, country, population=0):
    if population:
        full_name = city + ", " + country + ". Population: " + str(population) + "."
    else:
        full_name = city + ", " + country
    return full_name.title()

print(cities("santiago","chile"))

print(cities("berlim","alemanha",50.213))
