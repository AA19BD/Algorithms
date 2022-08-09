import csv
class Item:
    pay_rate=0.8#class attribute(static)
    all=[]
    def __init__(self, name: str, price: float, quantity=0):#type annotation
        # Run validations to the received arguments
        assert price >= 0, f'Price {price} is not greater  or equal to zero!'
        assert quantity >= 0, f'Quantity {quantity} is not greater  or equal to zero!'
        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        #Actions to execute
        Item.all.append(self)

    def calculate_total_price(self)->float:
        return self.price * self.quantity

    def apply_discount(self):
        self.price= self.price*self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv','r') as file:
            reader=csv.DictReader(file)
            items=list(reader)
        for item in items:
            Item(item['name'],float(item['price']),int(item['quantity']))
            # print(i)

    @staticmethod
    def is_integer(num):#takes argument(base function)
        if isinstance(num,float):
            return num.is_integer()#return true if Float is integer
        elif isinstance(num,int):
            return True
        return False

    def __repr__(self):
        return f'{self.name},{self.price},{self.quantity}'

# @classmethod
# Item.instantiate_from_csv()
# print(Item.all)

# @staticmethod
print(Item.is_integer(10.1))