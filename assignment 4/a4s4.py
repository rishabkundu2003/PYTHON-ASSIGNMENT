s = input("Enter a string")
n=s.split()
d=[]
for i in n:
    t=0
    for ch in i:
        t+=int(ch)
    d.append(t)
m1=1
m2=0
l1=1
l2=0
for i in range(1,len(d)):
    if d[i]>d[i-1]:
        l1+=1
    else:
        if l1>m1:
            m1=l1
            m2=l2
        l1=1
        l2=i
if l1>m1:
    m1=l1
    m2=l2

r=n[m2:m2+m1]
print("".join(r))
print(l1)
