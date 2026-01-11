a=[1,2,3,4,5]
b=[10,20,30,40,50]
nl=[]
k=2
for i in range(k):
    nl.insert(0,a[len(a)-1-i])
print(nl)
nl.extend(a[0:len(a)-k])
print(nl)
for i,item in enumerate(b):
    nl[i]+=item
print(nl)
