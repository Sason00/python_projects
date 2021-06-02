import random
import string

output = ""
length_of_pass = int(input("how long do you want your password? pick 8 to 12 "))
if length_of_pass < 8:
	length_of_pass = 8
elif length_of_pass > 12:
	length_of_pass = 12

def randomString(stringLength=1):
    letters= string.ascii_lowercase
    return ''.join(random.sample(letters,stringLength))

def randomSighn(stringLength=1):
    sighns = ["!", "@", "#", "$", "%", "^", "&", "*", "\\", "|", "," , ".", "-", "_", "=", "+"]
    rrr = int(random.random() * len(sighns))
    return sighns[rrr]

def randomDef():
    Defs = ["N", "str", "sighns"]
    ssss = int(random.random() * 3)
    sss = Defs[ssss]
    if sss == "N":
        return int(random.random() * 10)
    elif sss == "str":
        return randomString()
    elif sss == "sighns":
        return randomSighn()

for i in range(length_of_pass):
    output += str(randomDef())
print(output)
print(input("press enter to close"))

