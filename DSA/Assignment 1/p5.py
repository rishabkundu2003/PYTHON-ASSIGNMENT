def repeat(n):
    r=n[0]
    l=len(n)
    for i in range(1,l):
        if n[i]==n[i-1]:
            r+="*"
        else:
            r+=n[i]
    return r
print(repeat("aaabbbbx"))
