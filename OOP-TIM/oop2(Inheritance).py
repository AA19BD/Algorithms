class Pet:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def show(self):
        print(f'I am {self.name} and i am {self.age} years old')
    def speak(self):
        print('I dont know what I say')

class Cat(Pet):
    def __init__(self,name,age,color):
        super().__init__(name,age)
        self.color = color
    def speak(self):
        print("Meow")
    def show(self):
        print(f'I am {self.name} and i am {self.age} years old and I am {self.color}')
class Dog(Pet):
    def speak(self):
        print('Bark')


p=Pet('Tim',2)
p.speak()
c=Cat('bill',2,'black')
c.speak()
d=Dog('Doggy',2)
d.show()
