from prac_07.project import Project
from datetime import datetime

FILENAME = "projects.txt"
HEADER = "Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage"



def main():
    projects = load_data(FILENAME)

    menu()

    command = input(">> ").upper()
    while command != 'Q':
        if command == "L":
            file_name = input("File Name: ")
            projects = load_data(file_name)
        elif command == "S":
            file_name = input("File Name: ")
            save_data(file_name, projects)
        elif command == "D":
            display(projects)
        elif command == "F":
            date = datetime.strptime(input("dd/mm/yyyy"), '%d/%m/%Y')
            filter_projects(projects, date)
        elif command == "A":
            print("Add")
        elif command == "U":
            projects = update(projects)
        elif command == "Q":
            print("Quit")
        else:
            print("Bad Command")
        menu()
        command = input(">> ").upper()


def menu():
    print("""
L: Load
S: Save
D: Display
F: Filter (By Date)
A: Add
U: Update
Q: Quit""")


def load_data(file_name):
    file_handler = open(file_name, 'r')
    file_handler.readline()  # Clears Headers
    data = []
    for line in file_handler:
        parts = line.strip().split("\t")
        data.append(Project(parts[0], datetime.strptime(parts[1], "%d/%m/%Y"), int(parts[2]), float(parts[3]), int(parts[4])))
    file_handler.close()
    return data


def save_data(file_name, data):
    file_handler = open(file_name, 'w')
    print(HEADER, file=file_handler)
    for entry in data:
        print(f"{entry}", file=file_handler)
    file_handler.close()
    print(f"Data saved to: {file_name}")


def display(projects):
    print("Incomplete Projects:")
    incomplete_projects = [project for project in projects if not project.is_complete()]
    incomplete_projects.sort()
    for project in incomplete_projects:
        print_formatted(project)
    print("Completed Projects:")
    complete_projects = [project for project in projects if project.is_complete()]
    complete_projects.sort()
    for project in complete_projects:
        print_formatted(project)


def filter_projects(projects, date):
    filtered_projects = [project for project in projects if project.start_date > date]
    for project in filtered_projects:
        print_formatted(project)


def print_formatted(project):
    print(f"{project.name}, start: {project.start_date.strftime('%d/%m/%Y')}, priority {project.priority}"
          f", estimate: ${project.cost}, completion: {project.percentage}%")


def update(projects):
    return projects


main()
