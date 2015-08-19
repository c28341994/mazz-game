# -*- coding: utf-8 -*-
import random
import player
from gamehelper import*


class Maze:

    global player_row
    global player_column
    player_row = 6*[100]
    player_column = 6*[100]


    def __init__(self):         #初始化迷宮
        self.__maze =  [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                       [1,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                       [1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,1,0,1],
                       [1,0,0,1,0,0,0,1,1,0,0,0,1,0,0,1,0,0,0,1,0,0,1,0,1],
                       [1,0,0,0,0,0,0,0,0,1,1,0,1,0,0,1,0,1,1,0,0,1,0,0,1],
                       [1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,1,0,0,0,0,0,1],
                       [1,0,1,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,9,0,0,0,0,1],
                       [1,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1,1,0,1,0,1],
                       [1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,1,0,0,0,0,0,1,0,1],
                       [1,0,1,1,1,1,0,0,1,0,1,1,0,0,1,0,0,0,1,0,0,0,1,0,1],
                       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1],
                       [1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,1,0,1],
                       [1,0,0,0,0,1,1,0,1,1,1,1,0,0,1,0,0,0,1,0,0,0,0,0,1],
                       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                       [1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,1],
                       [1,0,0,1,0,0,0,1,0,0,1,1,1,0,0,1,0,0,1,0,0,0,0,0,1],
                       [1,0,0,0,0,1,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,1],
                       [1,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,1,0,0,1],
                       [1,0,0,0,0,0,0,1,1,1,0,1,1,1,0,1,0,0,1,0,0,0,0,0,1],
                       [1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,0,1],
                       [1,1,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                       [1,0,0,0,0,0,0,1,1,1,1,0,0,1,0,0,1,1,0,1,0,1,0,1,1],
                       [1,1,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1],
                       [1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,1,0,1,0,1],
                       [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

    def get_maze(self):

        return self.__maze

    def get_position(self,i):

        return player_row[i],player_column[i]

    def rand_position(self,who):                 #隨機玩家位置(可做瞬間移動發展)
        while 1:
            player_row[who] = random.randrange(0,24)
            player_column[who] = random.randrange(0,24)
            if self.__maze[player_row[who]][player_column[who]] == 0 :
                self.__maze[player_row[who]][player_column[who]] = who+2
                return player_row[who],player_column[who]

    def set_element(self,row,col,element):

		  self.__maze[row][col]  =  element


    def get_element(self,row,col):

         return self.__maze[row][col]

    def  set_position (self,who,row,col) :
          self.__maze[player_row[who]][player_column[who]] = 0
          player_row[who] = row
          player_column[who] = col
          self.__maze[player_row[who]][player_column[who]] = who+2

    def print_maze(self,p):                         #列印迷宮
        who = p.get_who()
        for i in range(0, 25, 1):
            for j in range(0, 25, 1):
                #if i>=player_row[who]-p.get_sense() and i<=player_row[who]+p.get_sense() and j>=player_column[who]-p.get_sense() and j<=player_column[who]+p.get_sense():
                    if self.__maze[i][j] == 0 :
                      print " ",               				  #無東西
                    #elif self.__maze[i][j] == who+2 :
                      #print("@"),
                    elif self.__maze[i][j] == 1 :
                      print("*"),                                 #牆壁
                    elif self.__maze[i][j] == 2 :
                      print("B"),                                 #boss
                    elif self.__maze[i][j] == 3 :
                      print("1"),                                 #玩家1
                    elif self.__maze[i][j] == 4 :
                      print("2"),                                 #玩家2
                    elif self.__maze[i][j] == 5 :
                      print("3"),                                 #玩家3
                    elif self.__maze[i][j] == 6 :
                      print("4"),                                 #玩家4
                    elif self.__maze[i][j] == 7 :
                      print("5"),                                 #玩家5
                    else:
                      print("$"),                                 #終點
                #else:
                    #print " ",
            print




    def judge_move(self,direct,who):                   #可走回傳1，牆壁回傳0
        if direct == "w":
            if self.__maze[player_row[who]-1][player_column[who]] == 0 or self.__maze[player_row[who]-1][player_column[who]] == 9:
                return 1
            else :
                return 0
        elif direct == "s":
            if self.__maze[player_row[who]+1][player_column[who]] == 0 or self.__maze[player_row[who]+1][player_column[who]] == 9 :
                return 1
            else :
                return 0
        elif direct == "a":
            if self.__maze[player_row[who]][player_column[who]-1] == 0 or self.__maze[player_row[who]][player_column[who]-1] == 9 :
                return 1
            else :
                return 0
        elif direct == "d":
            if self.__maze[player_row[who]][player_column[who]+1] == 0 or self.__maze[player_row[who]][player_column[who]+1] == 9 :
                return 1
            else :
                return 0
        else:
            return 0



    def move(self,direct,p):                         #執行玩家之移動
        who = p.get_who()
        out = 0
        conn = p.get_conn()
        while out == 0 :
            if self.judge_move(direct,who) == 1:
                out = 1
                if who != 0:
                    conn.send(str(out))
                self.__maze[player_row[who]][player_column[who]] = 0            #使原本位置變為0
                if direct == "w":
                    player_row[who] -= 1
                elif direct == "s":
                    player_row[who] += 1
                elif direct == "a":
                    player_column[who] -= 1
                else:
                    player_column[who] += 1
                if  self.__maze[player_row[who]][player_column[who]] != 9:
                    self.__maze[player_row[who]][player_column[who]] = who+2     #變成玩家後來位置

            else:
                if who != 0:
                    conn.send(str(out))
                print("此處不能走，請再輸入一次")
                direct = p.move()
        p.set_position(player_row[who],player_column[who])



    def out_maze(self,who,plist):                                             #判斷是否走到終點了
        if self.__maze[player_row[who]][player_column[who]] == 9 and plist[who].get_key() == 1:
            print("恭喜獲勝!!!")
            return 1
        else:
            return 0
