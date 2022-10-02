# Question 1:
nameFile = open('name.txt', 'w')
name1 = input("Enter name: ")
print(f"{name1}", file=nameFile)

nameFile.close()

# Question 2
fileName = open('name.txt', 'r')
name2 = fileName.readline()
print(f"Your name is {name2}")
fileName.close()

# Question 3
numbersFile = open('numbers.txt', 'r')
num1 = int(numbersFile.readline())
num2 = int(numbersFile.readline())
print(num1+num2)
numbersFile.close()

# Question 4
total = 0
fileNumbers = open('numbers.txt', 'r')
numbers = fileNumbers.readlines()
for x in numbers:
    total += int(x)
print(total)
fileNumbers.close()