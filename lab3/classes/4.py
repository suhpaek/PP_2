class Points:
    def __init__(self):
        self.x = int(input("enter x: "))
        self.y = int(input("enter y: "))
    
    def show(self):
        print(f'Point at ({self.x}, {self.y}) coordinates')
    
    def move(self):
        self.x = int(input("enter new x"))
        self.y = int(input("enter new y"))

    def distance_to(self, other_point):
        dis = ((other_point.x - self.x)**2 + (other_point.y - self.y)**2)**0.5
        print(f'Distance between two points is {round(dis, 2)}')
    
point1 = Points()
point1.show()

point2 = Points()
point2.show()

point1.distance_to(point2)