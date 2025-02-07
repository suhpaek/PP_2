def filter_prime(a):
    l=[]
    for i in a:
        n=int(i)
        if n<=1:
            continue
        if n==2:
            l.append(n)
            continue
        if n%2==0:
            continue
        pr= True
        for j in range(3, int(n**0.5)+1, 2):
            if n%j==0:
                pr= False
                break
        if pr:
            l.append(n)
    return l

a=input().split()
l= filter_prime(a)
print(l)

