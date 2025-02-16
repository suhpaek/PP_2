def even(n):
    for i in range(n+1):
        if (i%2==0):
            yield i
        

n=int(input())
for res in even(n):
    print(res, end=", ")
    