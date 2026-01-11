def lds(a,n):
    lds=[0]*n
    max=0
    for i in range(n):
        lds[i]=1
    for i in range(1,n):
        for j in range(i):
            if((a[i]<a[j])and (lds[i]<lds[j]+1)):
                lds[i]=lds[j]+1
    for i in range(n):
        if max<lds[i]:
            max=lds[i]
    return max
a=[15,27,14,38,63,55,46,65,85]
n=len(a)
print(lds(a,n))
