import math

num_sides = int(input())
side_length = float(input())

area = (num_sides*(side_length **2))/(4*math.tan(math.pi/num_sides))

print(int(area))