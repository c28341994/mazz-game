# -*- coding: utf8 -*-

import time
import socket

class Gamehelper:


    @classmethod
    def now_playing(cls,p,m,plist):
        who = p.get_who()
        if p.get_live()> 0 :
            cls.clear()
            m.print_maze(p)
            if who!= 0 :
                print ("現在是玩家\r")
                print (who)
                print ("的回合!\r")
                print
            else :
               print ("現在是Boss的回合!\r")
               print
            movement = p.movement(plist)
            if movement=='w' or  movement=='s' or  movement=='a' or  movement=='d' :
                   m.move(movement,p)
                   time.sleep(1)
            elif movement == "atk":
                   cls.direct = p.atk_pos()
                   cls.judgeatk(p,m,cls.direct,p.atk(),plist)
            elif movement == "noop":
                    pass
            elif movement == "close":
                    if who<3 :
                        cls.row ,cls.col =  plist[who+1].get_position()
                    else  :
                        cls.row ,cls.col =  plist[0].get_position()
                    if m.get_element(cls.row,cls.col) == 0 :

                          p.set_position(cls.row+1,cls.col)
                          m.set_position(who,cls.row+1,cls.col)


                    else :
                       print "You can't go to there"
                       time.sleep(2)
            else :
                  print "It's not a correct command"



        else :
                print "P",who,"  It's not your business "

                time.sleep(2)



    @staticmethod
    def clear():                                                    #強制清屏
        for i in range(40):
            print



    @classmethod
    def judgeatk(cls,p,m,direct,value,plist):
        cls.row ,cls.col = p.get_position()
        cls.atk = p.atk()
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
        elif  2 <  cls.element and cls.element <=7 :

           plist[cls.element-2].damaged(cls.atk)
           print "You deal ",cls.atk," damage to P",cls.element-2
           if plist[cls.element-2].get_live()<=0 :
                cls.row ,cls.col = plist[cls.element-2].get_position()
                m.set_element(cls.row,cls.col,0)
                print "P",cls.element-2,"you are  dead"
                if  plist[cls.element-2].get_key() == 1 :
				    plist[p.get_who()].set_key()
           time.sleep(3)
        elif  cls.element == 2 :

           plist[cls.element-2].damaged(p.get_who(),cls.atk,plist)
           print "You deal ",cls.atk," damage to Boss"
           if plist[cls.element-2].get_live()<=0 :
                cls.row ,cls.col = plist[cls.element-2].get_position()
                m.set_element(cls.row,cls.col,0)
                print "Boss",cls.element-2,"is  dead"
