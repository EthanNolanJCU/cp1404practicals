def main():
    """Main Function"""
    password = input("Enter password: ")
    minLength = 8
    password = get_password(minLength, password)

    asterisks(password)


def asterisks(password):
    print("*" * len(password))


def get_password(minLength, password):
    while len(password) < minLength:
        print("Password is must be atleast", minLength, "characters")
        password = input("Enter password: ")
    return password


main()