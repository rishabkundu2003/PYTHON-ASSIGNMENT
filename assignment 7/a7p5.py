x = 10
def f1():
    y = 20
    def f2():
        global x
        nonlocal y
        x = x + 5      
        y = y + 5      
        print("Global x:", x)
        print("Nonlocal y:", y)
    f2()
    print(y)
f1()
print(x)
