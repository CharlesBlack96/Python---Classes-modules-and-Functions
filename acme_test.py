
'''This mudule contains functions and assert statements
that create unit tests to test the functionality of most of my functions
throughout both acme.py and acme_reports.py. designed to help find bugs
in my code and also to make me think differently
about the code that i am writing to make it either
cleaner, more generic and more functional.'''


from acme import Product
from acme_reports import generate_products


def test_default_product_price():

    '''Test default product price being 10.'''

    prod = Product('Test Product')
    assert prod.price == 10


def test_default_product_weight():

    '''test default prduct weight being 20'''

    prod = Product('Test Product')
    assert prod.weight == 20


def test_default_product_flammability():

    '''test default product flammability is 0.5'''

    prod = Product('Test Product')
    assert prod.flammability == 0.5


def test_product_stealability():

    '''test stealability method of product class'''

    prod = Product('Test Product')
    quotient = prod.price / prod.weight
    assert (quotient < .5) is False


def test_product_stealability_2():

    '''test stealability method of product class'''

    prod = Product('Test Product')
    quotient = prod.price / prod.weight
    assert (quotient <= .5) is True


def test_product_stealability_3():

    '''test stealability method of product class'''

    prod = Product('Test Product')
    quotient = prod.price / prod.weight
    assert (quotient > .5) is False


def test_product_explode():

    '''test explode method of boxingglove class'''

    prod = Product('Test Product')
    product = prod.flammability * prod.weight
    assert (product > 10) == "...fizzle."
    assert (10 < product < 50) == "...Boom!"
    assert (product == 10) == "...BABOOM!!"


def test_product_punch():

    '''test punch method of boxingglove class'''

    prod = Product('Test Product')
    product = prod.weight
    assert (product < 5) == "That tickles."
    assert (5 <= product < 15) == "Hey that hurt!"
    assert (product >= 15) == "OUCH!"


def test_generate_products():

    '''
    Test the list size of the generate products function
    from the acme_reports module.
    '''

    product_list = generate_products()
    assert len(product_list) == 30
