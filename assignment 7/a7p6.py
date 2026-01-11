def display(*args):
    print(args)
    total = 0
    for num in args:
        total += num
    print("Sum:", total)
display(1, 2, 3)
display(5, 10, 15, 20)
