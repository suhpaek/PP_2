def gen(n):
    for i in range(n+1):
        yield i**2
        

n=int(input())
for sq in gen(n):
    print(sq)
    