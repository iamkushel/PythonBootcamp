#In python everything is an object and you can check object type using type function

l = [1,2,3,4,5]
print(type(l))

#Class name starts with a capital letter

class test(object):
    pass
#an attribute is a characteristic of an object. A method is a function of an object

#A function inside a class is called a method

class Dog(object):
    #class object Attritube,  meaning this attritube remains true throughout class
    species = 'mammal'
    def __init__(self,breed):  #the word breed is the attribute of the dog
        self.breed = breed
        print(breed)
sam = Dog(breed ='lab')
alex = Dog(breed = 'huskie')

print(sam.breed)
print(alex.species)



