# -*- coding: utf8 -*-

import random
from gamehelper import*

class Player :

   def  __init__(self,who):                                            #設定玩家血量、傷害
        self.__who = who
        self.__live = 1
        self.__hp = 10
        self.__dmg = 20
        self.__row = 0
        self.__column = 0
        
   def set_position(self,row,column):
        self.__row = row
        self.__column = column

   def get_who(self):
        return self.__who


   def get_position(self):
        return self.__row, self.__column

   def get_live(self):
        return self.__live 
   
   def  movement(self):                                                #決定玩家行動
        while 1:
           self.x = raw_input("Please enter what you want to do : ")
           if self.x == "mv":                                          #玩家選擇移動則回傳其欲移動方向 
              return self.move()
           elif self.x == "atk":                                       #玩家選擇攻擊，則回傳其攻擊力
              return "atk"
           elif self.x == "noop":    
              return "noop"
           elif self.x == "close":
               return "close"		   
           else:
              print "It's not a correct command"
   def  move(self):

       while 1:
         self.x = raw_input("Please enter where you want to go : ")
         if self.x=='w' or  self.x=='s' or  self.x=='a' or  self.x=='d' :
            return self.x
         else:
            print "It's not a correct command"
   def atk(self):

         return random.randrange(0,self.__dmg)
  
   def  damaged(self,value):
   
         self.__hp =  self.__hp - value
         print "P",self.__who,"have",self.__hp,"hp"
         if self.__hp <= 0 :
             self.__live = 0
            


 
   
if __name__ == "__main__" :


   p1 = player()

   x = p1.movement()

   print x       

   
   
