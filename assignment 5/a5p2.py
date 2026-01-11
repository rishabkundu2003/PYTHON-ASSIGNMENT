def sales(d):
    l=len(d[0])
    t=[0]*l
    for i in d:
        for j in range(l):
            t[j]=t[j]+i[j]
    m1=max(t)
    m2=min(t)
    print(t)
    print(m1)
    print(m2)
d=[[5,3,0,2],[7,0,2,1],[0,1,4,0]]
print(d)
print(sales(d))
