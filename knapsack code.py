n = int(input("Enter number of items: "))
items = []
for i in range(n):
    name = input("Enter item name: ")
    weight = float(input("Enter weight: "))
    profit = float(input("Enter profit: "))
    items.append((name, weight, profit))
c=20
r=[]
for name, weight, profit in items:
    r.append((profit / weight, name, weight, profit))
r.sort(reverse=True)
p=0
for name, weight, profit in r:
    if c>=weight:
        c-=weight
        p+= profit
    else:
        p+= profit*(c/weight)
        break
print("Maximum Profit:", p)
