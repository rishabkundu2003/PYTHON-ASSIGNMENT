l=[1,2,3,4,5]
k=3
def avg(l):
    s=0
    for el in l:
        s=s+el
    return s//len(l)
def varience(l):
    x=avg(l)
    s=0
    for i in l:
        s+=(i-x)**2
    return s
nl=[]
for i in range(len(l)-k+1):
    a=avg(l[i:i+k])
    v=varience(l[i:i+k])
    nl.append(tuple((a, v)))
print(nl)
