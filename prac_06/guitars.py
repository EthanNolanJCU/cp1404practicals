from prac_06.guitar import Guitar
print("My Guitars!")
my_guitars = []
name = input("Name: ")
while name != '':
    year = int(input("Year: "))
    cost = float(input("Price: ").strip('$'))
    my_guitars.append(Guitar(name, year, cost))
    print(f"{my_guitars[-1]} Added.")
    name = input("Name: ")

name_index = max(len(index.name) for index in my_guitars)
price_index = max(len(str(index.cost)) for index in my_guitars)

index = 1
for entry in my_guitars:
    vintage = '(vintage)' if entry.is_vintage() else ''
    print(f"Guitar {index}: {entry.name:>{name_index}} ({entry.year:>4}), worth $ {entry.cost:>{price_index},.2f}", vintage)
