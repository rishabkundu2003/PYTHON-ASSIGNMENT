def third(n):
    unique=list(set(n))
    unique.sort()
    if len(unique)<3:
        return "Yes"
    else:
        return unique[2]
print(third([34,89,54,20,50,76,10,45,90]))
