class Person:
    number_of_people=0

    def __init__(self,name):
        self.name = name
        Person.add_person()
    @classmethod
    def number_of_people1(cls):
        return cls.number_of_people

    @classmethod
    def add_person(cls):
        cls.number_of_people+=1

p1=Person('Jim')
# print(Person.number_of_people)
p2=Person('Bill')
# print(Person.number_of_people)

print(Person.number_of_people1())
Person.add_person()
print(Person.number_of_people1())

