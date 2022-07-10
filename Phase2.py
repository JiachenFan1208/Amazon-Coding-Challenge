#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 09:39:37 2022

@author: csimage

"""

import math
import random

class Block(object):
    def __init__(self, value, done, x,y):
        self.value = value
        self.done = done
        self.x = x
        self.y = y
    
    
    
graph = []
graph_len = 10
graph_hei = 10    

# Create map
for i in range(0,graph_hei):
    graph.append([])
    for j in range(0,graph_len):
        temp = Block(0,False,j,i)
        graph[i].append(temp)
        

# Set the initial coordinate

x = 0
y = 0

# Set the destination coordiante
x_des = 9
y_des = 9

# Randomly create 20 obstacles in different positions, except start point and destination.
# Set those coordinates which has obstacles to 1.
# The first dimension indicates y-coordinate, and the second dimension indicates x-coordinate.
obstacles_count = 0
obstacles = []

while(obstacles_count < 20):
    temp_x = random.randint(0,graph_len-1)
    temp_y = random.randint(0,graph_hei-1)
    
    if((temp_x != x and temp_y != y) and (temp_x != x_des and temp_y != y_des) and graph[temp_y][temp_x].value != 1):
        graph[temp_y][temp_x].value = 1
        obstacles.append(graph[temp_y][temp_x])
        obstacles_count += 1
    else:
        continue
        
final_ob = []        
    
for i in obstacles:
    final_ob.append("("+str(i.x)+","+str(i.y)+")")
    

print("\n"+"Obstacles: ")    
print(final_ob)  




# Use a stack to store steps
steps = []
steps.append(graph[0][0])

while(steps):
    
    current = steps[-1]
    print(current.x,current.y)
    
    neighbour_with_shortest_path = 0
    shortest_dis = math.sqrt(math.pow(x_des,2)+math.pow(y_des,2))
    
    if(current.x == x_des and current.y == y_des):
        print("You have reached the destination !")
        break
 
    else:
        # Try move down
        if(current.y + 1 < graph_hei and graph[current.y+1][current.x].value != 1 and graph[current.y+1][current.x].done != True):
            eucli_dis = math.sqrt(math.pow(x_des - current.x,2)+math.pow(y_des - (current.y+1),2))
            if eucli_dis < shortest_dis:
                shortest_dis = eucli_dis
                neighbour_with_shortest_path = 5
            
        
        # Try move bottom right
        if(current.y+1 < graph_hei and current.x+1 < graph_len and graph[current.y+1][current.x+1].value != 1 and graph[current.y+1][current.x+1].done != True):
            eucli_dis = math.sqrt(math.pow(x_des - (current.x+1),2)+math.pow(y_des - (current.y+1),2))
            if eucli_dis < shortest_dis:
                shortest_dis = eucli_dis
                neighbour_with_shortest_path = 4
            
        
        #Try move right
        if(current.x+1 < graph_len and graph[current.y][current.x+1].value != 1 and graph[current.y][current.x+1].done != True):
            eucli_dis = math.sqrt(math.pow(x_des - (current.x+1),2)+math.pow(y_des - current.y,2))
            if eucli_dis < shortest_dis:
                shortest_dis = eucli_dis
                neighbour_with_shortest_path = 3
            
        # Try move top right
        if(current.y-1 < graph_hei and current.x+1 < graph_len and graph[current.y-1][current.x+1].value != 1 and graph[current.y-1][current.x+1].done != True):
            eucli_dis = math.sqrt(math.pow(x_des - (current.x+1),2)+math.pow(y_des - (current.y-1),2))
            if eucli_dis < shortest_dis:
                shortest_dis = eucli_dis
                neighbour_with_shortest_path = 2
                
        # Try move top
        if(current.y - 1 < graph_hei and graph[current.y-1][current.x].value != 1 and graph[current.y-1][current.x].done != True):
            eucli_dis = math.sqrt(math.pow(x_des - current.x,2)+math.pow(y_des - (current.y-1),2))
            if eucli_dis < shortest_dis:
                shortest_dis = eucli_dis
                neighbour_with_shortest_path = 1
                
        # Try move top left
        if(current.y-1 < graph_hei and current.x-1 < graph_len and graph[current.y-1][current.x-1].value != 1 and graph[current.y-1][current.x-1].done != True):
            eucli_dis = math.sqrt(math.pow(x_des - (current.x-1),2)+math.pow(y_des - (current.y-1),2))
            if eucli_dis < shortest_dis:
                shortest_dis = eucli_dis
                neighbour_with_shortest_path = 8
                
        #Try move left
        if(current.x-1 < graph_len and graph[current.y][current.x-1].value != 1 and graph[current.y][current.x-1].done != True):
            eucli_dis = math.sqrt(math.pow(x_des - (current.x-1),2)+math.pow(y_des - current.y,2))
            if eucli_dis < shortest_dis:
                shortest_dis = eucli_dis
                neighbour_with_shortest_path = 7
                
        # Try move bottom left
        if(current.y+1 < graph_hei and current.x-1 < graph_len and graph[current.y+1][current.x-1].value != 1 and graph[current.y+1][current.x-1].done != True):
            eucli_dis = math.sqrt(math.pow(x_des - (current.x-1),2)+math.pow(y_des - (current.y+1),2))
            if eucli_dis < shortest_dis:
                shortest_dis = eucli_dis
                neighbour_with_shortest_path = 6

        
        
        
        
        
        
        if neighbour_with_shortest_path == 3:
            print("Right")
            steps.append(graph[current.y][current.x+1])
            graph[current.y][current.x].done = True
            continue
        elif neighbour_with_shortest_path == 4:
            print("Bottom-Right")
            steps.append(graph[current.y+1][current.x+1])
            graph[current.y][current.x].done = True
            continue
        elif neighbour_with_shortest_path == 5:
            print("Down")
            steps.append(graph[current.y+1][current.x])
            graph[current.y][current.x].done = True
            continue
        elif neighbour_with_shortest_path == 6:
            print("Bottom-Left")
            steps.append(graph[current.y+1][current.x-1])
            graph[current.y][current.x].done = True
            continue
        elif neighbour_with_shortest_path == 7:
            print("Left")
            steps.append(graph[current.y][current.x-1])
            graph[current.y][current.x].done = True
            continue
        elif neighbour_with_shortest_path == 8:
            print("Top-Left")
            steps.append(graph[current.y-1][current.x-1])
            graph[current.y][current.x].done = True
            continue
        elif neighbour_with_shortest_path == 1:
            print("Top")
            steps.append(graph[current.y-1][current.x])
            graph[current.y][current.x].done = True
            continue
        elif neighbour_with_shortest_path == 2:
            print("Top-Right")
            steps.append(graph[current.y-1][current.x+1])
            graph[current.y][current.x].done = True
            continue
        else:
            print("Back")
            graph[current.y][current.x].done = True
            steps.pop()
            steps[-1].done = False
            continue
            
        
        
final_solution = []        
    
for step in steps:
    final_solution.append("("+str(step.x)+","+str(step.y)+")")
    

print("\n"+"Final solution: ")    
print(final_solution)  
    


        