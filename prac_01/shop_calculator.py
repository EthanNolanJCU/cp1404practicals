itemCount = int(input("Number of items: "))
while itemCount <= 0:
    print("Invalid Number of Items")
    itemCount = int(input("Number of items: "))

total_cost = 0
for i in range(0, itemCount, 1):
    price = int(input("Price of item: "))
    total_cost += price

if total_cost >= 100:
    total_cost -= total_cost*0.1

print(total_cost)
