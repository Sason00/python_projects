tasks = []
while True:
    ask = input("if you want to add to the list new task write \"add\" \nif you want to see the list write \"my list\" ")
    if ask == "add":
        add = input()
        tasks.append(add)
    elif ask == "my list":
        show_tasks = []
        for i in tasks:
            show_tasks += str(tasks.index(i) + 1)
        print(tasks)
        print(show_tasks)
        todo = input("if you did a task write \"delete\" \nif no hit enter ")
        if todo == "delete":
            num = int(input()) - 1
            del tasks[num]
            del show_tasks[num]
    