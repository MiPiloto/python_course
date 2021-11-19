magicians = ["dave","ilusius","mr m"]

def show_magicians(array):
    for mage in array:
        print("The great " + mage.title())

show_magicians(magicians)


great_mages=[]
def make_great(array):
    
    while array:
        mages = "The great " + array.pop()
        great_mages.append(mages.title())
             

make_great(magicians[:]) # chamando função com a cópia de uma array, deixando a original inalterada
print(magicians)
print(great_mages)

def sandwich(*ing):   
    print("Your sandwich will be made with " + str(ing))

sandwich('mussarela', 'oregano')

def build_pizza(size,**ingredients):
    pizza = {}
    pizza['size'] = size
    for key,value in ingredients.items():
        pizza[key] = value 
    return pizza # tenha certeza que o return está for do laço for

my_pizza = build_pizza(12,cover='mussarela',spices='oregano',middle='frango',borda='recheada')
print(my_pizza)


def build_car(name,model,**extras):
    car = {}
    car['name'] = name
    car['model'] = model
    for key,value in extras.items():
        car[key]=value 
    return car # tenha certeza que o return está for do laço for

my_car = build_car("subaru","outback",color="blue",tow_package="True")
print(my_car)