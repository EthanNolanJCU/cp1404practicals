"""
get name
display menu
get choice
while choice != Q
   if choice == H
       display "hello" name
   else if choice == G
       display "goodbye" name
   else
       display invalid message
   display menu
   get choice
display finished message
"""

name = input("Enter Name: ")
menu = """(H)ello
(G)oodbye
(Q)uit"""
print(menu)
command = input(">>>").lower()

while command != 'q':
    if command == 'h':
        print("Hello " + name)
    elif command == 'g':
        print("Goodbye " + name)
    else:
        print("Invalid Choice")
    print(menu)
    command = input(">>>").lower()
print("Finished")

