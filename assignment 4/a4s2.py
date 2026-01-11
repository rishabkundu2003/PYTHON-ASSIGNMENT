s=input("Enter a string")
d=[]
for ch in s:              
    if ch.isdigit():      
        d.append(int(ch))
if not d:
    print("No digits found")
else:
    t=sum(d)
    a=t//len(d)
    m1=min(d)
    m2=max(d)
print("Sum", t)
print("Average", a)
print("Minimum", m1)
print("Maximum", m2)
