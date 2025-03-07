import math

def multiply(numbers):
    return math.prod(numbers)

a = list(map(int, input().split()))

print(multiply(a))