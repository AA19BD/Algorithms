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

    def __repr__(self):
        return f'{self.name},{self.price},{self.quantity}'


# item1 = Item("Phone", 100, 1)
# item1.apply_discount()
# print(item1.price)
# # print(item1.name)
#
# item2 = Item("Laptop", 1000, 3)
# item2.pay_rate=0.7
# item2.apply_discount()
# print(item2.price)
# # print(item2.name)
#
# print(item1.calculate_total_price())
# print(item2.calculate_total_price())

# print(Item.pay_rate)
# print(item1.pay_rate)


# print(Item.__dict__)#All attributes for Class level
# print(item1.__dict__)#All attributes for Instance level
item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)

print(Item.all)#Using __repr__ (magic method)

for instance in Item.all:
    print(instance.name)