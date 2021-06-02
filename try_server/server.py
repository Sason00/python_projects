import socket
from _thread import *
import sys
from multiprocessing import process

server = "10.100.102.9"
port = 5555
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("waiting for connection")


def read_pos(str):
    str = str.split(",")
    return int(str[0]), int(str[1])


def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])


pos = [(0, 0), (100, 100)]


def thread_clinet(conn, player):
    conn.send(str.encode(make_pos(pos[player])))
    reply = ""

    while True:
        try:
            data = read_pos(conn.recv(2048).decode())
            pos[player] = data

            if not data:
                print("disconnected")
                break
            else:
                if player == 1:
                    reply = pos[0]
                else:
                    reply = pos[1]
                print("recieved:", data)
                print("sending:", reply)

            conn.sendall(str.encode(make_pos(reply)))

        except:
            pass
    print("lost connection")
    conn.close()


current_players = 0
while True:
    conn, addr = s.accept()
    print("connected to", addr)

    start_new_thread(thread_clinet, (conn, current_players))
    current_players += 1
