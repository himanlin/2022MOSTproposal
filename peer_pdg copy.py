# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 07:22:55 2022

@author: mlchen
"""

import datetime
import random
import numpy as np
import pandas as pd
from pandas.core.frame import DataFrame


# b('D'-C) > 1('C'-C) > 0('C'-D)|('D'-D), 2 > b > 1
# parameters
b=1.35
alpha=0.5
u=0.6 #peer pressure
ROUNDS = 100
GROUP=1
iter=30000
L=128


class Grid():
    def __init__(self, size=L) -> None:
        tmp = [None]*size
        for i in range(size):
            tmp[i] = [False]*size
        self.grid = tmp

    def assign_location(self, x, y, individual):
        self.grid[y][x] = individual


class Agent():
    def __init__(self) -> None:
        self.peergroup = 0
        self.now_strategy = np.random.binomial(size=1,n=1,p=0.500)[0]
        self.past_strategy=[]
        self.payoff=[]

start_time = datetime.datetime.now()
data=[]
data2=[]
pressure=[0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]

for k in range(len(pressure)):
    for l in range(10):
        print(pressure[k])
        u=pressure[k]
        G_majority=[False]*GROUP
        Numbers=[False]*GROUP
        Defect=[False]*GROUP
        Cooperate=[]
        
        
        g = Grid()
        z=0
        # initialize
        f=0
        for y in range(L):
            for x in range(L):
                individual = Agent()
                g.assign_location( x, y, individual)
                player = g.grid[y][x]
                if player.now_strategy==1:
                    Numbers[player.peergroup]+=1
                    Defect[player.peergroup]+=1
                else:
                    f+=1
                    Numbers[player.peergroup]+=1
    
        Cooperate.append(f/(L*L))
        print(f/1024)
        for i in range(GROUP):
            if Numbers[i]-Defect[i]>=Defect[i]:
                G_majority[i]=0
            else:
                G_majority[i]=1
    
    
    
        for i in range(iter):
            if z>500:
                break;
            Defect=[False]*GROUP
            #calculate fraction of cooperate and majority strategy of groups
            f=0
            for y in range(L):
                for x in range(L):
                    player = g.grid[y][x]
                    if player.now_strategy==1:
                        Defect[player.peergroup]+=1
                    else:
                        f+=1
                    #payoff of each player                
                    if x!=0:
                        left=g.grid[y][x-1].now_strategy
                    else:
                        left=g.grid[y][L-1].now_strategy
                    if x!=L-1:
                        right=g.grid[y][x+1].now_strategy
                    else:
                        right=g.grid[y][0].now_strategy
                    if y!=0:
                        down=g.grid[y-1][x].now_strategy
                    else:
                        down=g.grid[L-1][x].now_strategy
                    if y!=L-1:
                        up=g.grid[y+1][x].now_strategy
                    else:
                        up=g.grid[0][x].now_strategy
                        
                    if player.now_strategy==1:
                            neighbor_c=4-left-right-up-down
                            if G_majority[player.peergroup]==1:
                             #   if neighbor_c*b!=player.payoff[-1]:
                                    player.payoff.append(neighbor_c*b)
                            else:
                                #if neighbor_c*b*(1-u) !=player.payoff[-1]:
                                    player.payoff.append(neighbor_c*b*(1-u))
                    else:
                            neighbor_c=4-left-right-up-down
                            if G_majority[player.peergroup]==1:
                            #    if neighbor_c*(1-u) !=player.payoff[-1]:
                                    player.payoff.append(neighbor_c*(1-u))
                            else:
                               # if neighbor_c !=player.payoff[-1]:
                                    player.payoff.append(neighbor_c)
            G_majority=[False]*GROUP        
            Cooperate.append(f/L^2)
            if f<1 or f>L^2-1:
                break;
            if f/L^2-1<0.01:
                z+=1
            for i in range(GROUP):
                if Numbers[i]-Defect[i]>=Defect[i]:
                    G_majority[i]=0
                else:
                    G_majority[i]=1
    
            #random update strategy
            x1=random.randint(0,L-1)
            y1=random.randint(0,L-1)
            x2=random.randint(0,L-1)
            y2=random.randint(0,L-1)
            while (x1==x2 and y1==y2) or(g.grid[y1][x1].now_strategy==g.grid[y2][x2].now_strategy and (f/(L^2-1)>0.01 or f/(L^2-1)<0.99)):
                x2=random.randint(0,L-1)
                y2=random.randint(0,L-1)
            if g.grid[y1][x1].payoff[-1]>g.grid[y2][x2].payoff[-1]:
                i1 = g.grid[y1][x1]
                i2 = g.grid[y2][x2]
            else:
                i2 = g.grid[y1][x1]
                i1 = g.grid[y2][x2]
            if np.random.binomial(size=1,n=1,p=1/(1+np.exp(i2.payoff[-1]-i1.payoff[-1])))[0]==1:
                    i2.past_strategy.append(i2.now_strategy)
                    i2.now_strategy=i1.now_strategy
            else:
                    i1.past_strategy.append(i1.now_strategy)
                    i1.now_strategy=i2.now_strategy
    
        data.append(Cooperate)
        data2.append(Cooperate[-1])

df=DataFrame(data)
df2=DataFrame(data2)
df.to_csv("output1g.csv")
df2.to_csv("output1g2.csv")
print(datetime.datetime.now()-start_time)
