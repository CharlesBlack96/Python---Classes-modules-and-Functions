from sprint9assignment.wallet import Wallet
import pytest

# when functions are called first class objects 
# this means that the function definition can be saved 
# to a variable and be passed around as a variable like anything
# else

#pytest fixture syntax
#pytest fixture are very handy when needing to represent 
#complex scenarios that the user needs to complete
#before running the unit tests on code 

#the @ sign is called a decorator
#it takes some function and extends its functionality
#enabling us to write code before and after it

#notice when the pytest fixture function is passed
# to another function we dont have envolking parenthasis
# because we are not calling the function we are passing
# it to another function and saying hey "you use it"

@pytest.fixture
def wallet_20():
    return Wallet(20)

@pytest.fixture
def empty_wallet():
    return Wallet()

#using the pytest fixture above i can
#  reduce my written code below and place 
# empty_wallet inside test_empty_wallet
# as a parameter instead of making a new variable
#ex) def test_empty_wallet(empty_wallet):
    # assert empty_wallet.balance == 0

def test_empty_wallet():
    empty_wallet = Wallet()
    assert empty_wallet.balance == 0

#using the pytest we can change this code below to the
# code underneath it
def test_wallet_20():
    assert Wallet(20).balance == 20

#def test_wallet_20(wallet_20):
    #assert wallet_20.balance ==20


#below i will have removed extra variables of wallet_20
#and insert the walet_20 function as a parameter
#created in test pytest fixture above

def test_wallet_20_spend_10(wallet_20):
    assert wallet_20.spend_cash(10) == 'remaining balance: 10'
    
def test_spend_all_cash(wallet_20):
    assert wallet_20.spend_cash(20) == 'remaining balance: 0'

#pytest fixture

