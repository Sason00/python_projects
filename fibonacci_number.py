x = 0
y = 1
z = x + y
for i in range(100):
    print(x)
    x = y
    y = z
    z = x + y
