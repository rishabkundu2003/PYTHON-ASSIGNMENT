def unique(l):
    l1= []
    for i in l:
        if i not in l1:
            l1.append(i)
    return l1
print(unique([1,2,2,3,3,3,4,4,5]))
