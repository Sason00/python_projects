import random

answers = []
counter1 = 0

def pick_level():
    global input1
    input1 = int(input("pick num between 1-4"))
    while input1 <= 0 or input1 > 4:
        input1 = int(input("pick num between 1-4"))
    ask()

def ask():
    global input2
    global input3
    input2 = int(input("pick the first num between 10-1000"))
    while input2 <= 9 or input2 > 1000:
        input2 = int(input("pick the first num between 10-1000"))
    input3 = int(input("pick the second num between 10-1000"))
    while input3 <= 9 or input3 > 1000:
        input3 = int(input("pick the second num between 10-1000"))
    check_what_question()

def grade(x, y):
    return1 = 100 * (int(x) / int(y))
    return return1

def ask_questions_num_1():
    global answers
    global counter1
    ran1 = random.randrange(input2, input3)
    ran2 = random.randrange(input2, input3)
    print("what is the answer?:" + str(ran1) + "+" + str(ran2))
    answer1 = float(input("write here the answer"))
    if ran1 + ran2 == answer1:
        print("your answer is correct!")
        answers.append(True)
    else:
        print("your answer isn't correct")
        answers.append(False)
    print("if you want to end the test write \"n\" and if you want to continue write \"y\"")
    answer2 = input()
    answer2 = answer2.lower()
    if answer2 == "y":
        ask_questions_num_1()
    elif answer2 == "n":
        for i in answers:
            if i:
                counter1 += 1
        print("there is ", counter1, " correct answers out of " + str(len(answers)) + " answers")
        print(print(grade(counter1, len(answers))))
        counter1 = 0
        answers = []
        pick_level()
    else:
        while not answer2 == "y" or not answer2 == "n":
            answer2 = input()
            answer2 = answer2.lower()
            if answer2 == "y":
                ask_questions_num_1()
            elif answer2 == "n":
                for i in answers:
                    if i:
                        counter1 += 1
                print("there is", counter1, "correct answers out of " + str(len(answers)) + " answers")
                print(print(grade(counter1, len(answers))))
                counter1 = 0
                answers = []
                pick_level()            
    
        
def ask_questions_num_2():
    global answers
    global counter1
    ran1 = random.randrange(input2, input3)
    ran2 = random.randrange(input2, input3)
    print("what is the answer?:" + str(ran1) + "-" + str(ran2))
    answer1 = float(input("write here the answer"))
    if ran1 - ran2 == answer1:
        print("your answer is correct!")
        answers.append(True)
    else:
        print("your answer isn't correct")
        answers.append(False)
    print("if you want to end the test write \"n\" and if you want to continue write \"y\"")
    answer2 = input()
    answer2 = answer2.lower()
    if answer2 == "y":
        ask_questions_num_2()
    elif answer2 == "n":
        for i in answers:
            if i:
                counter1 += 1
        print("there is", counter1, "correct answers out of " + str(len(answers)) + " answers")
        print(print(grade(counter1, len(answers))))
        counter1 = 0
        answers = []
        pick_level()
    else:
        while not answer2 == "y" or not answer2 == "n":
            answer2 = input()
            answer2 = answer2.lower()
            if answer2 == "y":
                ask_questions_num_2()
            elif answer2 == "n":
                for i in answers:
                    if i:
                        counter1 += 1
                print("there is", counter1, "correct answers out of " + str(len(answers)) + " answers")
                print(print(grade(counter1, len(answers))))
                counter1 = 0
                answers = []
                pick_level()    
def ask_questions_num_3():
    global answers
    global counter1
    ran1 = random.randrange(input2, input3)
    ran2 = random.randrange(input2, input3)
    print("what is the answer?:" + str(ran1) + "*" + str(ran2))
    answer1 = float(input("write here the answer"))
    if ran1 * ran2 == answer1:
        print("your answer is correct!")
        answers.append(True)
    else:
        print("your answer isn't correct")
        answers.append(False)
    print("if you want to end the test write \"n\" and if you want to continue write \"y\"")
    answer2 = input()
    answer2 = answer2.lower()
    if answer2 == "y":
        ask_questions_num_3()
    elif answer2 == "n":
        for i in answers:
            if i:
                counter1 += 1
        print("there is", counter1, "correct answers out of " + str(len(answers)) + " answers")
        print(print(grade(counter1, len(answers))))
        counter1 = 0
        answers = []
        pick_level()
    else:
        while not answer2 == "y" or not answer2 == "n":
            answer2 = input()
            answer2 = answer2.lower()
            if answer2 == "y":
                ask_questions_num_3()
            elif answer2 == "n":
                for i in answers:
                    if i:
                        counter1 += 1
                print("there is", counter1, "correct answers out of " + str(len(answers)) + " answers")
                print(print(grade(counter1, len(answers))))
                counter1 = 0
                answers = []
                pick_level()
def ask_questions_num_4():
    global answers
    global counter1
    ran1 = random.randrange(input2, input3)
    ran2 = random.randrange(input2, input3)
    print("what is the answer?:" + str(ran1) + "/" + str(ran2))
    answer1 = float(input("write here the answer"))
    if ran1 / ran2 == answer1:
        print("your answer is correct!")
        answers.append(True)
    else:
        print("your answer isn't correct")
        answers.append(False)
    print("if you want to end the test write \"n\" and if you want to continue write \"y\"")
    answer2 = input()
    answer2 = answer2.lower()
    if answer2 == "y":
        ask_questions_num_4()
    elif answer2 == "n":
        for i in answers:
            if i:
                counter1 += 1
        print("there is", counter1, "correct answers out of " + str(len(answers)) + " answers")
        print(print(grade(counter1, len(answers))))
        counter1 = 0
        answers = []
        pick_level()
    else:
        while not answer2 == "y" or not answer2 == "n":
            answer2 = input()
            answer2 = answer2.lower()
            if answer2 == "y":
                ask_questions_num_4()
            elif answer2 == "n":
                for i in answers:
                    if i:
                        counter1 += 1
                print("there is", counter1, "correct answers out of " + str(len(answers)) + " answers")
                print(grade(counter1, len(answers)))
                counter1 = 0
                answers = []
                pick_level()

def check_what_question():
    if input1 == 1:
        ask_questions_num_1()
    elif input1 == 2:
        ask_questions_num_2()
    elif input1 == 3:
        ask_questions_num_3()
    elif input1 == 4:
        ask_questions_num_4()

pick_level()

