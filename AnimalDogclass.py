class Animal(object):

    def __init__(self):
        print("I am animal")
    def whoami(self):
        print("I am an animal")
    def eat(self):
        print("i eat")

animal = Animal()
animal.whoami()

class Dog(Animal):

    def __int__(self):
        print("I am a Dog")
    def whoami(self):
        print("I am a mammal")
    def bark(self):
        print("wooooof")

dog = Dog()
dog.eat()
dog.bark()
