# -*- coding: utf8 -*-

import time

class Gamehelper:
    

    @classmethod 
    def now_playing(cls,p,m,plist):
            who = p.get_who()
            cls.clear()
            m.print_maze(who)
            print ("現在是玩家\r")
            print (who)
            print ("的回合!\r")
            print
            movement = p.movement()
            if movement=='w' or  movement=='s' or  movement=='a' or  movement=='d' :
                m.move(movement,p)
            elif movement == "atk":
                while 1:
                     cls.direct  = raw_input ("Where do you want to attack?")
                     if cls.direct=='w' or  cls.direct=='s' or  cls.direct=='a' or  cls.direct=='d' :               
                           cls.judgeatk(p,m,cls.direct,p.atk(),plist)
                           break
                     else :
                           print "It's not a correct command"
                              
   
    @staticmethod
    def clear():                                                    #強制清屏
        for i in range(40):
            print

    @classmethod 
    def judgeatk(cls,p,m,direct,value,plist):
        cls.col ,cls.row = p.get_position()
         
        if direct == 'w':
           cls.element = m.get_element(cls.row-1,cls.col)
        elif direct == 'a':
           cls.element = m.get_element(cls.row,cls.col-1)
        elif direct == 'd':
           cls.element = m.get_element(cls.row,cls.col+1)
        elif direct == 's':
           cls.element = m.get_element(cls.row+1,cls.col)
                  
        if cls.element == 0 or cls.element == 1:
           print "You deal massive damage to air"
           time.sleep(3)
        #elif  
           