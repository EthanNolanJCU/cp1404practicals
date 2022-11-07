from prac_07.project import Project
from datetime import datetime


def main():
    menu()
    command = input(">> ").upper()
    while command != 'Q':
        if command == "L":
            projects = load_data()
        elif command == "S":
            print("Save")
        elif command == "D":
            print("Display")
        elif command == "F":
            print("Filter")
        elif command == "A":
            print("Add")
        elif command == "U":
            print("Update")
        elif command == "Q":
            print("Quit")
        else:
            print("Bad Command")
        menu()
        command = input(">> ").upper()

    for project in projects:
        print(project)


def menu():
    print("""
L: Load
S: Save
D: Display
F: Filter (By Date)
A: Add
U: Update
Q: Quit""")


def load_data():
    file_name = input("File Name: ")
    file_handler = open(file_name, 'r')
    file_handler.readline()  # Clears Headers
    data = []
    for line in file_handler:
        parts = line.strip().split("\t")
        data.append(Project(parts[0], datetime.strptime(parts[1], "%d/%m/%Y"), int(parts[2]), float(parts[3]), int(parts[4])))
    return data


main()
