#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 09:39:37 2022

@author: csimage

"""

import math

class Block(object):
    def __init__(self, value, done, x,y):
        self.value = value # 0 means empty block, 1 means iti is an obstacle
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
        
# Set those coordinates which has obstacles to 1.
# The first dimension indicates y-coordinate, and the second dimension indicates x-coordinate.
graph[7][9].value = 1
graph[7][8].value = 1
graph[7][7].value = 1
graph[8][7].value = 1



# Set the initial coordinate

x = 0
y = 0

# Set the destination coordiante
x_des = 9
y_des = 9

# Use a stack to store steps
steps = []
steps.append(graph[0][0])


# When vehicle arrive a new block, it will check its 8 neighbours' validation,
# and choose the valid block which has the shortest distance to the destination to move.
# So this algorithm ensure the final solution has the shortest distance.

while(steps):
    
    current = steps[-1]
    print(current.x,current.y)
    
    neighbour_with_shortest_path = 0
    shortest_dis = math.sqrt(math.pow(x_des,2)+math.pow(y_des,2)) # Euclidean's distance
    
    if(current.x == x_des and current.y == y_des):
        print("You have reached the destination !")
        break
 
    else:
        # Find the nieghbours with shortest distance to the destination
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
    


        