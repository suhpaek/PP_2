class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self):
        self.length = int(input("length: "))
    
    def area(self):
        return self.length ** 2
    
shape = Shape()
print("shape area: ", shape.area())

square = Square()
print("square area: ", square.area())