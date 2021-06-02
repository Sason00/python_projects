a1 = input("ציון")
list1 = []
LLL = 0
for i in range(len(a1)):
    list1.append(float(a1[i]))
    LLL += list1[i]
print(LLL)

a2 = input("תלמידים")
list2 = []
LLLL = 0
for t in range(len(a2)):
    list2.append(float(a2[t]))
    LLLL += list2[t]
print(LLLL)

dd = 0
for j in range(len(a1)):
    dd += list1[j] * list2[j]
print(dd)
print("הממוצע הוא", dd / LLLL)
while true:
    i = 0
    i += 1
