def rev(n):
    for i in range(n, -1, -1):
        yield i
        

n=int(input())
for res in rev(n):
    print(res, end=" ")
    