n=input("Enter a string")
vc={}
v="aeiou"
for ch in n:
    if ch in v:
        if ch in vc:
            vc[ch]+=1
        else:
            vc[ch]=1
print(vc)
