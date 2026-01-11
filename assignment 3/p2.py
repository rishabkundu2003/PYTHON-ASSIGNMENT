c=0
while True:
    n = int(input("Enter a positive integer (0 or negative to stop): "))
    if n <= 0:
        break
    c+=1
    i=0
    while n > 9:
        s = 0
        t=n
        while t> 0:
            s = t % 10
            t //= 10
        n = s
        i += 1

    print("Iterations:", i)
    print("Final single digit:", n)
print("Total integers processed:", c)
