"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

def main():
    menuFunc()


def menuFunc():
    while True:
        menu = """
Enter a Value To Determine Status of your score
or type 'QUIT' to quit the porgram
"""
        print(menu)
        score = input(">> ")
        if score == "QUIT":
            break
        status = statusFunc(score)
        print(status)


def statusFunc(a):
    if a.isdigit():
        a = int(a)
    else:
        return "! Bad Command !"

    a = int(a)
    if a > 100 or a < 0:
        return "! Invalid Number !"
    elif a > 90:
        return "- Excellent"
    elif a > 50:
        return "- Passable"
    else:
        return "- Bad"

main()
