import random
import pytest
from acme import Product
from acme_reports import generate_products, adjectives, nouns


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
    assert (quotient < .5) == False

def test_product_stealability_2():
    '''test stealability method of product class'''
    prod = Product('Test Product')
    quotient = prod.price / prod.weight
    assert (quotient <= .5) == True

def test_product_stealability_3():
    '''test stealability method of product class'''
    prod = Product('Test Product')
    quotient = prod.price / prod.weight
    assert (quotient > .5) == False

def test_product_explode():
    '''test explode method of product class'''
    prod = Product('Test Product')
    product = prod.flammability * prod.weight
    assert (product > 10) == False
    assert (10 < product < 50) == False
    assert (product == 10) == True
    
#============================

def test_generate_products():
    '''test the list size of the generate products function
    from the acme_reports module '''
    product_list = generate_products()
    assert len(product_list) == 30
