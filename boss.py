from player import Player
import random

class Boss(Player):


    def __init__(self):
        super(Boss, self).__init__(0)
        self.__hp = 50
        self.__dmg = 3
        self.__turn = 0
    
    def movement(self):
        self.__turn += 1
        self.__action = ["mv","atk","close","noop"]
        self.__direct = ['w','a','s','d']
        self.__movement = random.choice(self.__action)
        
        if self.__movement =="mv" :
            print ("Boss choose mv!")
            return random.choice(self.__direct)
        else :
            if self.__movement =="atk" :
              print ("Boss choose atk!")
            elif self.__movement =="close" :
              print ("Boss choose close!")
            elif self.__movement =="noop" :
              print ("Boss choose noop!")
              
        return self.__movement
    def atk_pos(self) :
         self.__direct = ['w','a','s','d']
         return random.choice(self.__direct)


if __name__ == "__main__" :

    b = Boss()
    x = b.atk()
    print x
