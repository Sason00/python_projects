import random

words = [["g", "a", "m", "e"], ["p", "y", "t", "h", "o", "n"], [
    "m", "i", "n", "e", "c", "r", "a", "f", "t"], ["i", "p", "h", "o", "n", "e"]]
wrong_answers = 0
good_choices = []
w = ""


def start_game(word):
    global w
    global wrong_answers

    if len(good_choices) == 0:
        for g in word:
            good_choices.append("_ ")

    l = len(word)
    while True:
        if wrong_answers < 7:
            print("your word is: " + "".join(good_choices))
            print("your chances: " + str(wrong_answers) + "/7")
            input1 = input("guese a latter: ")
            if len(input1) != 1:
                print("you must pick one latter")
                input1 = input("guese a latter: ")
            if input1 in word:
                index = word.index(input1)
                good_choices[index] = str(input1)
                print("your latter is correct!")
                print("- - - - - - - - - - - - - -\n")
            else:
                print("your answer is incorrect!")
                print("- - - - - - - - - - - - - -\n")
                wrong_answers += 1
            if good_choices == word:
                print("you win")
                print("the word was " + "".join(word))
                break
        else:
            print("you lose!")
            print("the word was " + "".join(word))
            break


start_game(random.choice(words))
print(input("press Enter to exit"))
