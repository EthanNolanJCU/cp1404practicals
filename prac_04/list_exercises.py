def main():
    numbers = []
    for i in range(5):
        numberIn = int(input("Number: "))
        numbers.append(numberIn)

    print(f"First number: {numbers[0]}")
    print(f"Last number: {numbers[-1]}")
    print(f"Smallest number: {min(numbers)}")
    print(f"Largest number: {max(numbers)}")
    print(f"Average number: {sum(numbers)/len(numbers)}")


main()