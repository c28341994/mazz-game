# -*- coding: utf8 -*-
from player import Player
import maze
import random

class Boss(Player):

    global row
    global column
                              #Boss想攻擊或行走的方向
    row = 6*[100]
    column = 6*[100]



    def __init__(self):
        super(Boss, self).__init__(0,0)
        self.__hp = 50
        self.__dmg = 3
        self.__turn = 0
        self.__sense = 7      #Boss的感應範圍
        self.__damage = 5*[0]
        self.__boss_direct = 'w'

    def get_sense(self):
        return self.__sense

    def movement(self,plist):
        self.__turn += 1
        self.__action = ["mv","atk","close","noop"]
        self.__direct = ['w','a','s','d']
        self.__movement = random.choice(self.__action)

        M = maze.Maze()

        player_number = len(plist) - 1
        i=0
        while i<=player_number :                  #玩家與boss位置
            row[i],column[i] = plist[i].get_position()
            i+=1

        i=1
        while i<=player_number :
            if row[i] == row[0]-1 and column[i] == column[0] :      #是否有玩家位於Boss攻擊範圍
                self.boss_direct = 'w'
                print ("Boss choose atk up!")
                return "atk"
            if row[i] == row[0]+1 and column[i] == column[0] :
                self.boss_direct = 's'
                print ("Boss choose atk down!")
                return "atk"
            if row[i] == row[0] and column[i] == column[0]-1 :
                self.boss_direct = 'a'
                print ("Boss choose atk left!")
                return "atk"
            if row[i] == row[0] and column[i] == column[0]+1 :
                self.boss_direct = 'd'
                print ("Boss choose atk right!")
                return "atk"
            i+=1

        i=1
        while i<=player_number :
            if (row[i]<=row[0]-self.__sense or row[i]>=row[0]-self.__sense) and (column[i]<=column[0]-self.__sense or column[i]>=column[0]-self.__sense) :
                #若有人在Boss感應範圍內，則執行以下步驟判斷Boss該走哪裡
                if ((row[0]>=row[i] and column[0]>=column[i] and row[0]-row[i]>=column[0]-column[i]) or (row[0]>=row[i] and column[0]<=column[i] and row[0]-row[i]>=column[i]-column[0])) and M.get_element(row[0]-1,column[0]) == 0 :
                    print "Boss find player ",i," !!!"
                    print ("Boss choose move up!")
                    return 'w'
                if ((row[0]<=row[i] and column[0]>=column[i] and row[0]-row[i]>=column[0]-column[i]) or (row[0]<=row[i] and column[0]<=column[i] and row[0]-row[i]>=column[i]-column[0])) and M.get_element(row[0]+1,column[0]) == 0 :
                    print "Boss find player ",i," !!!"
                    print ("Boss choose move down!")
                    return 's'
                if ((row[0]>=row[i] and column[0]>=column[i] and row[0]-row[i]<=column[0]-column[i]) or (row[0]<=row[i] and column[0]>=column[i] and row[0]-row[i]<=column[i]-column[0])) and M.get_element(row[0],column[0]-1) == 0 :
                    print "Boss find player ",i," !!!"
                    print ("Boss choose move left!")
                    return 'a'
                if ((row[0]>=row[i] and column[0]<=column[i] and row[0]-row[i]<=column[0]-column[i]) or (row[0]<=row[i] and column[0]<=column[i] and row[0]-row[i]<=column[i]-column[0])) and M.get_element(row[0],column[0]+1) == 0 :
                    print "Boss find player ",i," !!!"
                    print ("Boss choose move right!")
                    return 'd'
                i+=1


        print ("Boss choose noop!")
        return "close"




    def atk_pos(self) :
         return self.boss_direct

    def  damaged(self,who,value,plist) :
         self.__hp =  self.__hp - value
         self.__damage[who] = self.__damage[who]+value
         print "Boss have",self.__hp,"hp"
         if self.__hp <= 0 :
             self.__live = 0
             rank = sorted(self.__damage)
             for i in range(5) :
                if  self.__damage[i] == rank[4] :
                     la = i
                     break
             plist[i].set_key()
