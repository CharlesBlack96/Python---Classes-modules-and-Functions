
'''
MY SECOND EXAMPLE OF CODE DOCUMENTATION
In this inventory report i provide code that
gives me all the results requested by the instructions
of the inventory report section of my sprint9assignment.
'''


import random


# Useful to use with random.sample or random.choice to generate names
adjectives = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
nouns = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def name():

    '''
    Name function returns a noun with a descriptor in a string made
    from a randomly chosen adj from the adj list above, then a space,
    and then a randomly chosen noun after the space.
    '''

    rand_adj = random.choice(adjectives)
    rand_nouns = random.choice(nouns)
    return rand_adj + ' ' + rand_nouns


def price():
    
    '''
    This price function returns a random integer
    between 5 and 100 to represent
    the price of the product.
    '''
   
    return random.randint(5,100)


def weight():

    '''
    this weight function returns a random integer between 5 and 100 to represent 
    the weight of the product.
    '''

    return random.randint(5,100)


def flammability():

    '''
    The flammability function returns a random float between 0.0 and 2.5 to
    represent the rating of a products flammability.
    '''

    return random.uniform(0.0, 2.5)


def product_tuple():

    '''
    The product_tuple function returns a tuple containing a list of all the
    results of each of the functions above creating a product tuple with a
    list of descriptive attributes of a random product.
    '''

    return (name(), price(), weight(), round(flammability(), 1))


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
        product_list.append(product_tuple())

    return product_list

# ====================================


def generate_names_list(num_products=30):

    '''
    The generate_names_list functions isolates returns
    a just list of 30 names
    such as the random ones found in the product_tuple
    above. each individual name
    is originally created by using the function name()
    at the top of the page
    which uses the adj and nouns list.
    '''

    names_list = []
    for item in range(num_products):
        names_list.append(product_tuple()[0])

    return names_list


def unique_val_of_names():

    '''
    The unique_val_of_names function counts the number of
    unique values
    or names help inside the list of 30 randomly
    generated names created
    by the generate_names_list function. will result in
    a different number
    each time due to randomness of the generate_names_list
    fucntion.
    '''

    num_of_unique = len(set(generate_names_list()))

    return num_of_unique


# ====================================


def generate_price_list(num_products=30):

    '''
    The generate_price_list function generates a
    list of 30 random prices correlating with
    a hypothetical list of 30 random products.
    '''

    price_list = []
    for item in range(num_products):
        price_list.append(product_tuple()[1])

    return price_list


def avg_price_of_prods():

    '''
    The avg_price_of_prods functiontakes takes in a newly
    generated list of random
    'product' prices each time and returns a number that
    represents the average of all 30 numbers
    in that list showing the average 'price' of 30 products.
    '''

    return sum(generate_price_list()) / len(generate_price_list())


# ====================================


def generate_weight_list(num_products=30):

    '''
    The generate_weight_list function generates a list
    of 30 random weights correlating with
    a hypothetical list of 30 random products.
    '''

    weight_list = []
    for item in range(num_products):
        weight_list.append(product_tuple()[2])

    return weight_list


def avg_weight_of_prods():

    '''
    The avg_weight_of_prods functiontakes takes in a
    newly generated list of random
    'product' weights each time and returns a number
    that represents the average of all 30 numbers
    in that list showing the average 'weight' of 30
    randomly generated products.    '''

    return sum(generate_weight_list()) / len(generate_weight_list())


# ====================================


def generate_flam_list(num_products=30):

    '''
    The generate_flam_list function generates
    a list of 30 random flammability
    ratings correlating with
    a hypothetical list of 30 random products.
    '''

    flam_list = []
    for item in range(num_products):
        flam_list.append(product_tuple()[3])

    return flam_list


def avg_flam_of_prods():

    '''
    The avg_flam_of_prods function takes takes in
    a newly generated list of random
    'product' flammability ratings each time and
    returns a number that represents
    the average of all 30 numbers in that list showing
    the average 'flammability rating'
    of 30 randomly generated products.
    '''
    return sum(generate_flam_list()) / len(generate_flam_list())

# ====================================


def inventory_report():
    '''
    The inventory_report function returns a tuple relationg to the 30 
    randomly generated productsa from the generated_products function towards
    the top of the page. relating to take list and all the functions used as the 
    parameters to this function we are returned a single tuple with a list inside
    showing the
    number of unique names in the list, the average price of the products
    in the list, the avegare weight of the products in the lise, ect....
    '''

    return (unique_val_of_names(),
            round(avg_price_of_prods(), 1),
            round(avg_weight_of_prods(), 1),
            round(avg_weight_of_prods(), 1),
            round(avg_flam_of_prods(), 1))


print(generate_flam_list())
print(avg_flam_of_prods())
print(inventory_report())
