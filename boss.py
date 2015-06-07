from player import Player

class Boss(Player):


    def __init__(self):

        self.__hp = 50
        self.__dmg = 0
    
    
    def test(self):
        pass





if __name__ == "__main__" :

    b = boss()
    x = b.atk()
    print x
