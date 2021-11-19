from random import randint

class Die ():

    def __init__(self,sides):
        self.sides = sides

    def roll_die(self):
        roll = randint(0,self.sides)
        print(roll)


six_sides = Die(6)

six_sides.roll_die()
six_sides.roll_die()
six_sides.roll_die()
six_sides.roll_die()
six_sides.roll_die()
six_sides.roll_die()
six_sides.roll_die()
six_sides.roll_die()
six_sides.roll_die()
six_sides.roll_die()


print("Now a ten sides die!\n")
ten_sides = Die(10)

ten_sides.roll_die()
ten_sides.roll_die()
ten_sides.roll_die()
ten_sides.roll_die()
ten_sides.roll_die()
ten_sides.roll_die()
ten_sides.roll_die()
ten_sides.roll_die()
ten_sides.roll_die()
ten_sides.roll_die()


print("One HUNDRED sides!\n")
one_hundred_sides = Die(100)

one_hundred_sides.roll_die()
one_hundred_sides.roll_die()
one_hundred_sides.roll_die()
one_hundred_sides.roll_die()
one_hundred_sides.roll_die()
one_hundred_sides.roll_die()
one_hundred_sides.roll_die()
one_hundred_sides.roll_die()
one_hundred_sides.roll_die()
one_hundred_sides.roll_die()