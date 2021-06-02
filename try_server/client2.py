from network import Network

n = Network()

while True:
    input1 = input("what do you want to send?")
    n.send(input1)
