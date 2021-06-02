import time

input1 = input("put a number: ")

list1 = []
num = 0
times = 0

for i in input1:
    list1.append(i)
print(list1)

while len(list1) != 1:
    for j in list1:
        num += int(j)
    print(num)
    list1 = []
    for j in str(num):
        list1.append(j)
    print(list1)
    num = 0
    times += 1
print("times:", times, "\n", "number:", num)

# 134959
