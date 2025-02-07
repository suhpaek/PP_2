class Shape:
    def area(self):
        return 0
    
class Rectangle(Shape):
    def __init__(self):
        dimen = str(input("Enter length and width: ")).split()
        self.length = int(dimen[0])
        self.width = int(dimen[1])
    
    def area(self):
        return self.length * self.width
    
shape = Shape()
print("shape area: ", shape.area())

rectangle = Rectangle()
print("rectangle area: ", rectangle.area())