from item import Item
class Phone(Item):
    pay_rate = 0.5  # Ov
    all=[]
    def __init__(self,name: str, price: float, quantity=0,broken_phones=0):
        #Call to super function to have access to all attributes/methods
        super().__init__(name, price, quantity)
        #Validation
        assert broken_phones>=0,f'Broken_phones {broken_phones} is not greater  or equal to zero!'
        # Assign to self object
        self.broken_phones=broken_phones

        Phone.all.append(self)