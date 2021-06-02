import eel

eel.init(r"C:\Users\Ariel\Desktop\python_projects\eel")

eel.start("\\main.html", block=False)


@eel.expose
def py_print_color(c):
    print(c)


@eel.expose
def py_check(user_name, password):
    if user_name == "ariel" or user_name == "Ariel":
        if password == "oren" or password == "Oren":
            print("correct")
            return None
        print("not correct")
        return None
    print("not correct")


while True:
    eel.sleep(1)
