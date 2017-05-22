class Circle(object):

    #class object attribute
    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius
        print(self.radius)

    def area(self):
        #radius = radius ** 2 * pi
        print(self.radius ** 2 * Circle.pi) #here pi is a class attribute so we use Circle.pi

    def new_radius(self, new_radius=1):
        self.radius = new_radius

c = Circle(radius = 10)
c.area()

print(c.radius)
c.new_radius(20)
c.area()
