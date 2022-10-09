def main():
    numbers = []
    for i in range(5):
        numbers.append(int(input("Number: ")))

    print(f"First number: {numbers[0]}")
    print(f"Last number: {numbers[-1]}")
    print(f"Smallest number: {min(numbers)}")
    print(f"Largest number: {max(numbers)}")
    print(f"Average number: {sum(numbers)/len(numbers)}")

    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']
    userInput = input("Enter Username")
    if (userInput in usernames):
        print("Access Granteded")
    else:
        print("Access Denied")
main()


