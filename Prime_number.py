from time import sleep


def check(n):
    for i in range(2, n//2):
        #print(n % i)
        if n % i == 0:
            return False
    return True


for i in range(100001058, 10000000000000000):
    i += 1
    if i % 2 == 0 or i % 5 == 0 or i % 10 == 0:
        print(i, False)
    else:
        print(i, check(i))
        sleep(0.05)
