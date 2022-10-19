def main():
    email_to_name = {}

    while True:
        user_email = input("Email: ")
        if user_email == "":
            break

        name = get_name_func(user_email)

        yes_list = ["yes", "ye", "y", "1", ""]
        no_list = ["no", "n"]
        user_name_correct = input(f"Is your name {name}? (Y/N)").lower()

        if user_name_correct in no_list:
            name = input("Enter name: ")
        elif user_name_correct not in yes_list:
            print("Bad Input: ")
            print(user_name_correct + " - Not Valid")
            break
        email_to_name[user_email] = name

    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def get_name_func(email):
    return " ".join(email.split("@")[0].split(".")).title()


main()
