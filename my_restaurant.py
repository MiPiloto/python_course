from class_Restaurant import Restaurant

restaurant01 = Restaurant("louis'","italian")
print(restaurant01.restaurant_name)
print(restaurant01.cuisine_type)
print(restaurant01.number_served)

restaurant01.number_served = 3
print(restaurant01.number_served)

restaurant01.set_number_served(5)
print(restaurant01.number_served)

restaurant01.increment_number_served(2)
print(restaurant01.number_served)

restaurant01.describe_restaurant()
restaurant01.open_restaurant()

restaurant02 = Restaurant("nissan","japanese")
print(restaurant02.restaurant_name)
print(restaurant02.cuisine_type)

restaurant02.describe_restaurant()
restaurant02.open_restaurant()

restaurant03 = Restaurant("kebab","arabic")
print(restaurant03.restaurant_name)
print(restaurant03.cuisine_type)

restaurant03.describe_restaurant()
restaurant03.open_restaurant()