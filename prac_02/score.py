"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

def main():
    score = float(input("Enter score: "))
    status = statusFunc(score)
    print(status)

def statusFunc(a):
    if a > 100 or a < 0:
        return "Invalid score"
    elif a > 90:
        return "Excellent"
    elif a > 50:
        return "Passable"
    else:
        return "Bad"

main()
