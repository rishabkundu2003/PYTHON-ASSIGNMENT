def maximum(a,b,c):
    max=0
    if a>b and a>c:
        max=a
    elif b>a and b>c:
        max=b
    else:
        max=c
    return max
print(maximum(12,34,1))
