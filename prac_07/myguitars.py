from prac_07.guitar import Guitar

FILENAME = "guitars.csv"


def main():
    guitars = load(FILENAME)
    guitars.sort()
    print("Current Guitars: ")
    for guitar in guitars:
        print(guitar)

    print("New Guitars:")
    new_guitars = []
    name = input("Name: ")
    while name != '':
        year = int(input("Year: "))
        cost = float(input("Price: ").strip('$'))
        new_guitars.append(Guitar(name, year, cost))
        print(f"{new_guitars[-1]} Added.")
        name = input("Name: ")

    guitars += new_guitars
    guitars.sort()
    for guitar in guitars:
        print(guitar)

    save(FILENAME, guitars)


def load(filename):
    file = open(filename, 'r')
    guitars = []
    for line in file:
        parts = line.strip().split(',')
        guitars.append(Guitar(parts[0], int(parts[1]), float(parts[2])))
    file.close()
    return guitars


def save(filename, data):
    file_handler = open(filename, 'w')
    for entry in data:
        print(f"{entry.name},{entry.year},{entry.cost}", file=file_handler)


main()