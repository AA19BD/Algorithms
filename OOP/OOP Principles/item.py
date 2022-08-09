import csv
class Item:
    pay_rate=0.8#class attribute(static)
    all=[]
    def __init__(self, name: str, price: float, quantity=0):#type annotation
        # Run validations to the received arguments
        assert price >= 0, f'Price {price} is not greater  or equal to zero!'
        assert quantity >= 0, f'Quantity {quantity} is not greater  or equal to zero!'
        # Assign to self object
        self.__name = name
        self.__price = price
        self.quantity = quantity

        #Actions to execute
        Item.all.append(self)

    @property
    def price(self):
        return self.__price

    def apply_increment(self,inc):
        self.__price= self.__price+self.__price*inc


    @property#Decorator-for Read-Only Attribute(Getter)
    def name(self):
        return self.__name

    @name.setter
    def name(self,value):
        if len(value)>10:
            raise Exception('The value too long!')
        else:
            self.__name=value

    def calculate_total_price(self)->float:
        return self.__price * self.quantity

    def apply_discount(self):
        self.__price= self.__price * self.pay_rate

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
        return f'{self.__class__.__name__}Class({self.name},{self.__price},{self.quantity})'


    #Abstraction
    def __connect(self):
        pass
    def __prepare_body(self):
        pass
    def __send(self):
        pass

    def send_email(self):
        self.__connect()
        self.__prepare_body()
        self.__send()