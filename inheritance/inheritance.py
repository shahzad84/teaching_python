class Mammal:
    def walk(self):
        print("walk")

class Dog(Mammal):#in this class we just have to pass Mammal : now dog class is inherited for mammal class
    def bark(self):
        print("bark")

class Cat(Mammal):
    pass #we don't want our class to do anything we just use "pass"

dog1=Dog()
dog1.walk()
dog1.bark()
