def string(s):
    uc=0
    lc=0
    for ch in s:
        if ch.isupper():
            uc+=1
        else:
            lc+=1
    return uc,lc
print(string("EDUCation"))
