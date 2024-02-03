# we use classes to define new types


class Point:#Point is follow naming convention
    # constroctor(__init__) is a function that gets called at the time of creating object.
    def __init__(self,x,y):
        self.x=x#we are using self to reference the current object and then we set x attribute.
        self.y=y
    def move(self):
        print("move")
    def draw(self):
        print("draw")

'''
point1=Point()#here we define an object of a class
point1.x=13
print(point1.x)
point1.draw()


#NOTE: each object is different instance of a class

point2=Point()
# print(point2.x)# it will through error because x is not attribute of point2
point2.draw()

'''

#using constructor
point=Point(12,23)
print(point.x)
