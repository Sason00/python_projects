import getpass

users = []
passwords = []

def ask():
    global input1
    input1 = input('if you have user name write "loggin" \nif not write "create":')
ask()

while True:
    if input1 == "create":
        user_name = input("enter your name: ")
        user_password = getpass.getpass("enter your password: ")
        users.append(user_name)
        passwords.append(user_password)
    elif input1 == "loggin":
        checks = 0
        Uinput = input("user name: ")
        Pinput = getpass.getpass("user password: ")
        if Pinput in passwords and Uinput in users and users.index(Uinput) == passwords.index(Pinput):
            print("work")
        else:
            print("password or user name undefind")
    ask()

print(users, passwords)
