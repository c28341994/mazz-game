# -*- coding: utf8 -*-

class Gamehelper:
    

    @classmethod 
    def now_playing(cls,p,m):

            cls.clear()
            m.print_maze()
            print ("現在是玩家\r"),
            print (p.get_who()),
            print ("的回合!\r"),
            print
            movement = p.movement()
            if movement=='w' or  movement=='s' or  movement=='a' or  movement=='d' :
                m.move(movement,p)
    
    @staticmethod
    def clear():                                                    #強制清屏
        for i in range(40):
            print

    

