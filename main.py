# -*- coding: utf-8 -*-
"""import gevent.monkey
gevent.monkey.patch_socket()
"""
import maze, player, boss, socket, gevent

from gamehelper import*

HOST = ''
PORT = 8888

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created'

try:
    s.bind((HOST, PORT))
except socket.error , msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()

s.listen(5)



M = maze.Maze()


p = [boss.Boss()]
row,column = M.rand_position(0)
p[0].set_position(row,column)

i = 1
threads = []
player_number = input("Please enter the number of player : ")
while i <= player_number:
    conn ,addr = s.accept()
    conn.send("Welcome to __ __ __")
    p.append(player.Player(i,conn))
    conn.send(str(i))

    row,column = M.rand_position(i)
    p[i].set_position(row,column)
    i+=1

i = 1
while i <= player_number:
    threads.append(gevent.spawn(Gamehelper.client,p[i],M,p,player_number))
