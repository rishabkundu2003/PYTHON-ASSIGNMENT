def check(d,key):
    if key in d.keys():
        print("present", d[key])
    else:
        print("not")
d={'a':100,'b':200,'c':300}
key='b'
check(d,key)
