class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        print(self.restaurant_name.title() + " is a good place to eat, and has the best " + self.cuisine_type + " cuisine!." )
    
    def open_restaurant(self):
        print(self.restaurant_name.title() + " is now open!")

    def set_number_served(self, served):
        self.number_served = served
    
    def increment_number_served(self,increment):
        self.number_served += increment

class IceCreamStand(Restaurant): #classe filha de Restaurant
    def __init__(self, restaurant_name, cuisine_type,):
        super().__init__(restaurant_name, cuisine_type,)
        self.flavors = ["chocolate","morango","baunilha"]

    def show_flavors(self): #método da classe filha
        for flavor in self.flavors:
            print(flavor.title())

my_iceCream = IceCreamStand("penguim","ice cream") #instancia da classe filha
my_iceCream.show_flavors()

      


