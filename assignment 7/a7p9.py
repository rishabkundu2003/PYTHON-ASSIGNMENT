def hcf(a, b):
    while b != 0:
        a, b = b, a % b
    return a
result = hcf(12, 18)
print("HCF is:", result)
