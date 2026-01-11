a=input("Enter 1st string")
b=input("Enter 2nd string")
c=[]
for ch in a:
    if ch not in b and ch not in c:
        c.append(ch)
if not c:
    print("Not missing")
else:
    print("missing", "".join(c))
