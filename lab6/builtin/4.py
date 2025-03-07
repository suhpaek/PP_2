import time
import math

num = int(input("Enter a number: "))
delay = int(input("Enter delay in milliseconds: "))

time.sleep(delay / 1000) 

sqrt_result = math.sqrt(num)

print(f"Square root of {num} after {delay} milliseconds is {sqrt_result}")