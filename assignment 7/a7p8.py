def lcm(a, b):
    if a == 0 or b == 0:
        return 0
    x, y = a, b
    while y:
        x, y = y, x % y
    gcd = x
    return abs(a * b)//gcd
result = lcm(12, 18)
print("LCM is:", result)
