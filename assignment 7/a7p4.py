def f1():
    def f2():
        print("This is the inner function")
    f2()
f1()
