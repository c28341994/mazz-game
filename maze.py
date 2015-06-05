# -*- coding: utf8 -*-
import random
import player 



class Maze:

    global player_row
    global player_column
    player_row = 6*[100]
    player_column = 6*[100]
    
    
    def __init__(self):         #初始化迷宮
        self.maze = [[1,1,1,1,1,1,1,1],
                     [1,0,0,1,0,1,9,1],
                     [1,0,1,0,0,1,0,1],
                     [1,0,0,1,0,0,0,1],
                     [1,1,0,1,0,1,1,1],
                     [1,0,0,0,0,1,0,1],
                     [1,0,1,1,0,0,0,1],
                     [1,1,1,1,1,1,1,1]]


    def rand_position(self,who):                 #隨機玩家位置(可做瞬間移動發展)
        while 1:
            player_row[who] = random.randrange(0,7)
            player_column[who] = random.randrange(0,7)
            if self.maze[player_row[who]][player_column[who]] == 0 :
                self.maze[player_row[who]][player_column[who]] = who+2
                return player_row[who],player_column[who]          


            


    def now_playing(self,p):

            self.clear()
            self.print_maze()
            print ("現在是玩家\r"),
            print (p.get_who()),
            print ("的回合!\r"),
            print
            movement = p.movement()
            if movement=='w' or  movement=='s' or  movement=='a' or  movement=='d' :
              self.move(movement,p)
            

    def print_maze(self):                         #列印迷宮
        for i in range(0, 8, 1):
            for j in range(0, 8, 1):
                if self.maze[i][j] == 0 : 
                  print " ",                                  #無東西
                elif self.maze[i][j] == 1 : 
                  print("*"),                                 #牆壁
                elif self.maze[i][j] == 2 : 
                  print("B"),                                 #boss
                elif self.maze[i][j] == 3 : 
                  print("1"),                                 #玩家1
                elif self.maze[i][j] == 4 : 
                  print("2"),                                 #玩家2
                elif self.maze[i][j] == 5 : 
                  print("3"),                                 #玩家3
                elif self.maze[i][j] == 6 : 
                  print("4"),                                 #玩家4
                elif self.maze[i][j] == 7 : 
                  print("5"),                                 #玩家5  
                else:
                  print("$"),                                 #終點
            print



    def judge_move(self,direct,who):                   #可走回傳1，牆壁回傳0
        if direct == "w":
            if self.maze[player_row[who]-1][player_column[who]] == 0 or self.maze[player_row[who]-1][player_column[who]] == 9:
                return 1
            else :
                return 0
        elif direct == "s":
            if self.maze[player_row[who]+1][player_column[who]] == 0 or self.maze[player_row[who]-1][player_column[who]] == 9 :
                return 1
            else :
                return 0
        elif direct == "a":
            if self.maze[player_row[who]][player_column[who]-1] == 0 or self.maze[player_row[who]-1][player_column[who]] == 9 :
                return 1
            else :
                return 0
        elif direct == "d":
            if self.maze[player_row[who]][player_column[who]+1] == 0 or self.maze[player_row[who]-1][player_column[who]] == 9 :
                return 1
            else :
                return 0
        else:
            return 0



    def move(self,direct,p):                         #執行玩家之移動
        who = p.get_who()
        out = 0
        while out == 0 :
            if self.judge_move(direct,who) == 1:
                out = 1
                self.maze[player_row[who]][player_column[who]] = 0            #使原本位置變為0
                if direct == "w":
                    player_row[who] -= 1
                elif direct == "s":
                    player_row[who] += 1
                elif direct == "a":
                    player_column[who] -= 1
                else:
                    player_column[who] += 1
                if  self.maze[player_row[who]][player_column[who]] != 9:   
                    self.maze[player_row[who]][player_column[who]] = who+2     #變成玩家後來位置

            else:
                print("此處不能走，請再輸入一次")
                direct = raw_input("Please enter where you want to go : ")
        p.set_position(player_row[who],player_column[who])


        
    def out_maze(self,who):                                             #判斷是否走到終點了
        if self.maze[player_row[who]][player_column[who]] == 9:
            print("恭喜獲勝!!!")
            return 1
        else:
            return 0

    def clear(self):                                                    #強制清屏
        for i in range(40):
            print

    def get_position(self,row,column,who):
        player_row[who] = row
        player_column[who] = column
        



    
#***********************************************************************

if __name__ == "__main__":


    
    
    
    M = Maze()                              #設定迷宮及初始位置
    M.rand_position(1)
    M.print_maze()
        
    








