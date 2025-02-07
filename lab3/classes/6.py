inp = str(input("Enter a numbers: ")).split(' ')
nums = [int(x) for x in inp]
fp = lambda x: x > 1 and all(x % i != 0 for i in range(2,int(x)))
prime = list(filter(fp, nums))
print(prime)