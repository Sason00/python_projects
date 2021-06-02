import random

is_test = True
input1 = 0

def ask():
    global input1
    while input1 <= 0 or input1 > 4:
        input1 = int(input("תבחר מספר מ1-4:"))

def ask_if_end_the_test():
    global input4
    pass
def test():
    ask()

    input2 = int(input("תבחר מספר ראשון מתחום מספרים בין 1 ל1000"))
    input3 = int(input("תבחר מספר ראשון מתחום מספרים בין 1 ל1000"))


    input4 = "y"
    counter1 = 0

    while input4 == "y":
        counter1 += 1
        if input1 == 1:
            random_num1 = random.randrange(input2, input3)
            random_num2 = random.randrange(input2, input3)
            print("שאלה : כמה זה " + str(random_num1) + "+" + str(random_num2) + " ?")
            input5 = float(input("תכתוב כאן את התשובה:"))
            if input5 == random_num1 + random_num2:
                print("תשובה נכונה!")
            else:
                print("תשובה שגויה")
            if counter1 % 2 == 0:
                input4 = input("רוצה לעשות עוד שאלה? אם כן תכתוב y אם לא תכתוב n")
                input4 = input4.lower()
                if input4 == "y":
                    pass
                elif input4 == "n":
                    ask()
                else:
                    while input4 != "n" and input4 != "y":
                        input4 = input("רוצה לעשות עוד שאלה? אם כן תכתוב y אם לא תכתוב n")
                        input4 = input4.lower()
                        if input4 == "y":
                            pass
                        elif input4 == "n":
                            break
            


while is_test:
    test()
