email_to_name = {}

while True:
    user_email = input("Email: ")
    if user_email == "":
        break

    name = " ".join(user_email.split("@")[0].split(".")).title()

    yes_list = ["yes", "ye", "y", "1", ""]
    no_list = ["no", "n"]
    user_name_correct = input(f"Is your name {name}? (Y/N)").lower()

    if (user_name_correct in yes_list):
        pass
    elif user_name_correct in no_list:
        name = input("Enter name: ")
    else:
        print("Bad Input")
        print(user_name_correct)
        break
    email_to_name[user_email] = name

for email, name in email_to_name.items():
    print(f"{name} ({email})")
