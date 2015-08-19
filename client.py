# -*- coding: utf-8 -*-

import socket
import sys
import os
import pickle

def clear():                                                    #強制清屏
    for i in range(40):
        print

HOST = '192.168.1.103'
PORT = 8888

try:
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

except socket.error, msg:
    print 'Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1]
    sys.exit();

print 'Socket Created'

s.connect((HOST,PORT))

welcome  = s.recv(1024)
print welcome

who = int(s.recv(4))
print who

while 1:
    nowwho = int(s.recv(4))
    print nowwho


    row =int(s.recv(4))
    print row
    column = int(s.recv(4))
    print column

    sense = int(s.recv(4))
    print sense
    data = s.recv(8196)
    maze = pickle.loads(data)
    clear()
    for i in range(0, 25, 1):
        for j in range(0, 25, 1):
            if i>= row-sense and i<= row+sense and j>=column-sense and j<=column+sense:
                if maze[i][j] == 0 :
                  print (" "),             				       #無東西
                elif maze[i][j] == who+2 :
                  print("@"),
                elif  maze[i][j] == 1 :
                  print("*"),                                 #牆壁
                elif  maze[i][j] == 2 :
                  print("B"),                                 #boss
                elif  maze[i][j] == 3 :
                  print("1"),                                 #玩家1
                elif  maze[i][j] == 4 :
                  print("2"),                                 #玩家2
                elif  maze[i][j] == 5 :
                  print("3"),                                 #玩家3
                elif  maze[i][j] == 6 :
                  print("4"),                                 #玩家4
                elif  maze[i][j] == 7 :
                  print("5"),                                 #玩家5
                else:
                  print("$"),                                 #終點
            else:
                print " ",
        print

    whoseturn = s.recv(2048)
    print whoseturn

    if who == nowwho:
        motion = raw_input("Please enter what you want to do : ")
        s.send(motion)
        if motion == "mv" :
            out = 0
            while out == 0 :

                direct = raw_input("Please decide where you want to go : ")
                s.send(direct)
                out = int(s.recv(4))
                if out == 0:
                    print("此處不能走，請再輸入一次")

        elif motion ==  "atk" :
            direct = raw_input("Please input direct you decide : ")
            s.send(direct)


os.system("pause")
