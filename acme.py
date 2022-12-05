
'''This message serves me as an example
of my first documentation
of my own code.
What is this code?. What is it doing?
This is the code for my initial part of my
sprint9 assignment for bloomtech institute.
Here i work on providing classes to represent
info for a company products.

all projects you care about should have a readme and
propper documentation and an open source LISCENCE!!!!!
SO YOUR CANT SUE YOUR COMPANY!!

ex) mit liscence
haven_mit liscence

enable others to legally use your code..necessary
'''


import random


class Product:

    '''
    this is the class docsting
    '''

    def __init__(self,
                 name,
                 price=10,
                 weight=20,
                 flammability=0.5,
                 identifier=random.randint(1000000, 9999999)):
        '''
        This is my __init__ function. It sets the default settings for
        the attributes of my product class.
        '''
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier

    def stealability(self):
        '''
        stealability method. Depending on the products price and weight we are
        able to calculate how stealable an item is with this function.
        '''
        quotient = self.price / self.weight
        if quotient < .5:
            return "Not so stealable..."
        if .5 <= quotient < 1.0:
            return "Kinda stealable."

        return "Very stealable!"
        
    def explode(self):
        '''
        explode method. depending of the products flammability score and the 
        weight of the product we use those values in this function to determine
        if a product will fizzle, boom, or baboom!
        '''
        product = self.flammability * self.weight
        if product > 10:
            return "...fizzle."
        if 10 <= product < 50:
            return "...Boom!"

        return "...BABOOM!!"


class BoxingGlove(Product):

    '''
    This is my BoxingGlove child class that inherits attributes from my product class and 
    has slightly different and/or entirely new methods of its own.
    '''

    def __init__(self,
                 name,
                 price=10,
                 weight=10,
                 flammability=0.5,
                 identifier=random.randint(1000000, 9999999)):
        super().__init__(name,
                         price=10,
                         weight=10,
                         flammability=0.5,
                         identifier=random.randint(1000000, 9999999))
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.idenitifier = identifier

    def explode(self):
        '''
        explode method returns "...its a glove."
        '''
        return "...its a glove."

    def punch(self):
        '''
        punch method. on the "weight" of the product the method
        will return weather or not a punch hurts with a 3 different strings.

        '''
        if self.weight < 5:
            return "That tickles."
        if 5 <= self.weight > 15:
            return "Hey that hurt!"

        return "OUCH!"
