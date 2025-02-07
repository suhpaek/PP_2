def uniq(li):
    li2 = []
    for i in li:
        if i not in li2:
            li2.append(i)
    print(li2)

li = list(map(int, input().split()))
uniq(li)