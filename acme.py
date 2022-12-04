'''This message serves me as an example
of my first documentation
of my own code.
What is this code?.....what is it doing?
this is the code for my initial part of my 
sprint9 assignment for bloomtech institute.
here i work on providing classes to represent and provide info for a companies products.
'''


import random

class Product:

    def __init__(self, name, price=10, weight=20, flammability=0.5, identifier=random.randint(1000000,9999999)):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier

    def stealability(self):
        quotient = self.price / self.weight
        if quotient < .5:
            return "Not so stealable..."
        if .5 <= quotient < 1.0:
            return "Kinda stealable."
        else:
            return "Very stealable!"
        
    def explode(self):
        product = self.flammability * self.weight
        if  product > 10:
            return "...fizzle."
        if 10 <= product < 50:
            return "...Boom!"
        else:
            return "...BABOOM!!"

# if __name__ == '__main__':
#     prod = Product('A cool toy')

# print(prod.name)
# print(prod.price)
# print(prod.weight)
# print(prod.flammability)
# print(prod.identifier)

# print(prod.stealability())
# print(prod.explode())

class BoxingGlove(Product):

    def __init__(self, name, price=10, weight=10, flammability=0.5, identifier=random.randint(1000000,9999999)):
        super().__init__(name, price=10, weight=10, flammability=0.5, identifier=random.randint(1000000,9999999))
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.idenitifier = identifier

    def explode(self):
        return "...its a glove."

    def punch(self):
        if self.weight < 5:
            return "That tickles."
        if 5 <= self.weight > 15:
            return "Hey that hurt!"
        else:
            return "OUCH!"

# if __name__ == '__main__':
#     prod = BoxingGlove('A cool toy')

# print(prod.name)
# print(prod.price)
# print(prod.weight)
# print(prod.flammability)
# print(prod.identifier)
# print(prod.explode())
# print(prod.punch())