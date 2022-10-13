"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}

for code, states in CODE_TO_NAME.items():
    print(f"{code:<3} is {CODE_TO_NAME[code]}")


state_code = input("Enter short state: ")
while state_code != "":
    state_code = state_code.upper()
    try:
        print(f"{state_code} is {CODE_TO_NAME[state_code]}")
    except:
        print("Invalid short state")
    state_code = input("\nEnter short state: ")



