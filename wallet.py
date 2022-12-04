class Wallet:

    #first thing to run when we make a new class
    #outline required user provided input values here
    #parameters with default values assigned aree optional
    def __init__(self, initial_amount=0):
        #save the user provide initial_amount as an attribute
        #self refers to whateve object im working with 
        self.balance = initial_amount

    #spend cahs METHOD
    def spend_cash(self, amount):
        if self.balance < amount:
            return 'not enough money'
        else:
            self.balance = self.balance - amount
            return f'remaining balance: {self.balance}'

    def add_cash(self, amount):
        self.balance = self.balance + amount
        return f'new balance of: ${self.balance}'

    


    #__repr__ method
    # changhes how the 'object' looks when it is printed out
    #the rpesence of the self keyword allows me to access or modify
    # class attributes within this function
    def __repr__(self):
        return f'wallet with balance of: ${self.balance}'

if __name__ == '__main__':
    wallet1 =  Wallet(100)
   
