d1={'key1':1, 'key2':3, 'key3':2}
d2={'key1':1, 'key2':2}
for i,j in d1.items():
    if i in d2 and d2[i]==j:
        print(f"{i}: {j} is present")
