# -*- coding: utf8 -*-
import maze  
import player 

      
p = [0]



M = maze.Maze()                              #設定迷宮及初始位置

i = 1
player_number = input("Please enter the number of player : ")
while i <= player_number:
    p.append(player.Player(i))
    row,column = M.rand_position(i)
    p[i].set_position(row,column)  
    i+=1

i = 1
while i <= player_number:   
    M.now_playing(p[i]) 
    if M.out_maze(i) == 1:
        break
    if i == player_number:
        i = 0
    i += 1

