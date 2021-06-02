import tkinter as tk 
from tkinter import ttk

screen = tk.Tk()
screen.resizable(0, 0)

File = open("users.rtf", "r").read()
users_list = str(File).split(" ")


users = []
for i in users_list:
    users.append(tuple(i.split("-")))
print(users)
# print(users)
# passwords = []
b1 = ttk.Button(screen)
n2 = ttk.Button(screen)
user_name_entry = ttk.Entry(screen)
password_entry = ttk.Entry(screen)
password_confirm_entry = ttk.Entry(screen)
error_label = tk.Label(screen)
submit1 = ttk.Button(screen)
get_username = ttk.Entry(screen)
get_password = ttk.Entry(screen)
submit2 = ttk.Button(screen)
access_label = tk.Label(screen)
return_button = ttk.Button(screen)


def submit_new_user(username, password1, password2):
    global error_label
    if len(username) < 2 or len(password1) < 2:
        error_label = tk.Label(screen, text="username and password must be at least 6 caracters ")
        error_label.grid(column=0, row=4)
        return
    if password1 == password2:
        for i in users:
            if username in i or password1 in i:
                print(i, username, password1)
                error_label = tk.Label(screen, text="username or password has already been taken")
                error_label.grid(column=0, row=4)
                return
        users.append((username, password1))
        file_to_append = open("users.rtf", "a")
        file_to_append.write(username + "-" + password1 + " ")
        main_screen()
    else:
        error_label = tk.Label(screen, text="password aren't same")
        error_label.grid(column=0, row=4)
        
def submit_user(username, password):
    global access_label
    global return_button
    for i in users:
        if username in i:
            if password in i:
                get_username.destroy()
                get_password.destroy()
                submit2.destroy()
                access_label = tk.Label(screen, text="you logged in")
                access_label.grid(column=0, row=0)
                return_button = ttk.Button(screen, text="return", command=main_screen)
                return_button.grid(column=0, row=1)
                return
    get_username.destroy()
    get_password.destroy()
    submit2.destroy()
    access_label = tk.Label(screen, text="username or password is incorrect")
    access_label.grid(column=0, row=0)
    return_button = ttk.Button(screen, text="return", command=main_screen)
    return_button.grid(column=0, row=1)



def new_acount():
    global user_name_entry
    global password_entry
    global password_confirm_entry
    global submit1
    b1.destroy()
    b2.destroy()

    user_name = tk.StringVar()
    password = tk.StringVar()
    password_confirm = tk.StringVar()
    user_name_entry = ttk.Entry(screen, textvariable=user_name)
    user_name_entry.grid(column=0, row=0)
    user_name_entry.bind("<Button-1>", lambda x: error_label.destroy())
    password_entry = ttk.Entry(screen, show="*", textvariable=password)
    password_entry.grid(column=0, row=1)
    password_entry.bind("<Button-1>", lambda x: error_label.destroy())
    password_confirm_entry = ttk.Entry(screen, show="*", textvariable=password_confirm)
    password_confirm_entry.grid(column=0, row=2)
    password_confirm_entry.bind("<Button-1>", lambda x: error_label.destroy())
    submit1 = ttk.Button(screen, text="submit", command=lambda: submit_new_user(user_name.get(), password.get(), password_confirm.get()))
    submit1.grid(column=0, row=3)

def log_in():
    global get_username
    global get_password
    global submit2
    b1.destroy()
    b2.destroy()

    user_name = tk.StringVar()
    password = tk.StringVar()
    get_username = ttk.Entry(screen, textvariable=user_name)
    get_username.grid(column=0, row=0)
    get_password = ttk.Entry(screen, textvariable=password, show="*")
    get_password.grid(column=0, row=1)
    submit2 = ttk.Button(screen, text="submit", command=lambda: submit_user(user_name.get(), password.get()))
    submit2.grid(column=0, row=2)

def main_screen():
    global b1
    global b2
    user_name_entry.destroy()
    password_entry.destroy()
    password_confirm_entry.destroy()
    error_label.destroy()
    submit1.destroy()
    get_username.destroy()
    get_password.destroy()
    submit2.destroy()
    access_label.destroy()
    return_button.destroy()
    b1 = ttk.Button(screen, text="loggin", command=log_in)
    b1.grid(column=0, row=0)

    b2 = ttk.Button(screen, text="create new acount", command=new_acount)
    b2.grid(column=1, row=0)

if __name__ == "__main__":
    main_screen()

screen.mainloop()