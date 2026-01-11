def remove(l):
    l1=[]
    for i in range(len(l)):
        a=l[:i]
        b=l[i+1:]
        c=a+b
        l1.append(c)
    return l1
n=[1,1,2,2,3,4,3,1]
print(n)
print(remove(n))
