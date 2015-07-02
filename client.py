import socket
import sys
import os

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

num = s.recv(4)
print num

while 1:
    who = s.recv(4)
    whoseturn = s.recv(2048)
    print whoseturn
    if who == num:
        motion = raw_input("Please enter what you want to do : ")
        s.send(motion)
        if motion == "mv" or "atk":
            direct = raw_input("Please input direct you decide : ")
            s.send(direct)

os.system("pause")
