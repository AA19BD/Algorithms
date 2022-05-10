from item import Item
from phone import Phone
from keyboard import Keyboard


item1=Item('My_Keyboard',100,1)
item1.apply_increment(0.2)
item1.apply_discount()
print(item1.price)


item1.send_email()