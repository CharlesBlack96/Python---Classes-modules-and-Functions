# pylint: disable=unused-variable

'''
In this inventory report i provide code that
gives me all the results requested by the instructions
of the inventory_report section of my sprint9assignment.
'''


import random
from acme import Product


# Useful to use with random.sample or random.choice
# to generate names
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable',
              'Improved']

NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


# ====================================


def generate_products(num_products=30):

    '''
    The generate_products function creates
    a list of 30 tuples that were created by
    using a for loop and the function
    above that created a tuple with one list
    of desciptive attributes of a function.
    returns 30 lists of attributes relating to
    30 random made up products.
    '''

    product_list = []
    for item in range(num_products):
        rand_adj = random.choice(ADJECTIVES)
        rand_nouns = random.choice(NOUNS)
        name = rand_adj + ' ' + rand_nouns
        price = random.randint(5, 100)
        weight = random.randint(5, 100)
        flammability = random.uniform(0.0, 2.5)

        product_list.append(Product(name=name,
                                    price=price,
                                    weight=weight,
                                    flammability=flammability))

    return product_list


def inventory_report(product_list):

    '''
    The inventory_report function returns a tuple relationg
    to the 30 randomly generated productsa from the
    generated_products function towards the top of the page.
    relating to take list and all the functions used as the
    parameters to this function we are returned a single
    tuple with a list inside showing the
    number of unique names in the list, the average price of
    the products in the list, the avegare weight of the
    products in the lise, ect....
    '''

    num_of_unique = len(set(item.name[0] for item in product_list))
    avg_price = str(sum(item.price[1] for
                    item in product_list) / len(product_list))
    avg_weight = str(sum(item.weight[2] for
                     item in product_list) / len(product_list))
    flammability = str(sum(item.flammability[3] for
                       item in product_list) / len(product_list))

    return (num_of_unique, avg_price, avg_weight, flammability)
