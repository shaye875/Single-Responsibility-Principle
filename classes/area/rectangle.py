from shape import *

class Rectangle(Shape):
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def area(self):
        return self.y*self.x