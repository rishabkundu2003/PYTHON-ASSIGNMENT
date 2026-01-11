d={'dress':23, 'pant':45, 'shoe':12, 'bungle':55, 'book':8}
x=list(d.values())
x.sort(reverse=True)
x=x[:3]
for i in x:
    for j in d.keys():
        if(d[j]==i):
            print(j,i)
