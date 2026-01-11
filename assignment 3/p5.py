v=int(input())
c=0
lg=1
l=1
for i in range(8):
    n=int(input("Enter a no"))
    if n>v:
        l=l+1
    else:
        c=c+1
        if l>lg:
            lg=l
        l=l+1
    v=n
c=c+1
if l>lg:
    lg=l
print(c)
print(lg)
