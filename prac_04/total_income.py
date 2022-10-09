"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomeList = []
    numMonth = int(input("How many months? "))

    for month in range(1, numMonth + 1):
        income = float(input(f"Enter income for month {month} : "))
        incomeList.append(income)

    incomeOutput(incomeList)


def incomeOutput(incomeList):
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, len(incomeList) + 1):
        income = incomeList[month - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))


main()