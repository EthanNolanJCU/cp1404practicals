import random

def main():
    num = int(input("How many Quick Picks: "))

    for i in range(num):
        picks = []
        for j in range(6):
            x = 0
            while (x in picks) or (x == 0):
                x = random.randint(1, 45)
            picks.append(x)
        picks.sort()
        printArr(picks)


def printArr(arr):
    for i in arr:
        print(f"{i:>2}", end=" ")
    print("")

main()