def div34(n):
    for i in range(n+1):
        if i%3==0 and i%4==0:
            yield i
        

n=int(input())
for res in div34(n):
    print(res, end=" ")
    