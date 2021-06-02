def lehagel(num):
    if num % 10 == 0:
        return num
    else:
        return (int(str(num)[0]) + 1) * 10

input1 = input("put here an ID number: ")
Review_number = input1[-1]
input1 = input1[0:-1]
print(input1)
ID = ""
Review_number2 = 0
for i in range(len(input1) - 1):
    if i % 2 == 0:
        ID = ID + str(int(input1[i]) * 2)
    else:
        ID = ID + input1[i]
print(ID)
for j in ID:
    Review_number2 += int(i)
Review_number2 = lehagel(Review_number2) - Review_number2
print(Review_number2)
