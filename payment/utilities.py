class Transaction():
    
    def __init__(self,price): 
        # gets the information to set up the transaction 
        # amount, gateway    
        self.price = price
    
    
    def process_transaction(self): 
        # processes the current (self) transaction and returns 
        # a boolean indicating if the transaction was successful 
        # given the payment gateway. 
        # connection to web services. 
        return True

