"SA for TSP"
import numpy as np
import pandas as pd
import math
from numpy import random
import matplotlib.pyplot as plt
#getting inputs-------------------------
n=52
d=pd.read_csv("b52_dataset.csv")
cord=d.to_numpy().copy()
#distance matrix-----------------------
dist=np.zeros((n,n))
for i in range(n):
    for j in range(n):
        dist[i,j]=math.sqrt((cord[i,1]-cord[j,1])**2+(cord[i,2]-cord[j,2])**2)
#cost func-----------------------------
def cost(s):
    y=np.zeros((n,n))
    for i in range(n):
        if i==n-1:
            y[s[i]-1,s[0]-1]=1
        else:
            y[s[i]-1,s[i+1]-1]=1
    cost=np.sum(y*dist)
    return cost
#tour gen func------------------------------
def new_tour(s):
    i=random.randint(n)
    j=random.randint(n)
    while i==j:
         j=random.randint(n)
    new_tour=s.copy()
    new_tour[i]=s[j]
    new_tour[j]=s[i]
    return new_tour
#initial state-------------------------------------
s=np.arange(52)
z=cost(s)
record_z=np.array([0])
mean_z=np.mean(record_z) 
#parameters--------------------------------------
T=300
alpha=0.995
N=30
T_final=0.000001
#Main loop --------------    
while T>T_final:
    for i in range(N):
        new_s=new_tour(s)
        new_z=cost(new_s)
        if new_z<z:
            s=new_s.copy()
            z=new_z.copy()
            record_z=np.r_[record_z,new_z]
            mean_z=np.r_[mean_z,np.mean(record_z)]
        elif random.rand()<math.exp(-1*((new_z-z)/T)):
            s=new_s.copy()
            z=new_z.copy()
            record_z=np.r_[record_z,new_z]
            mean_z=np.r_[mean_z,np.mean(record_z)]
    T=T*alpha
#Plots-----------------------------
opt=np.zeros(len(record_z))+7544             
record_z=np.delete(record_z,[0])    
plt.plot(record_z)    
plt.plot(opt)
#-------------------------------------
print("best answer= ",z)        
    
    
    
    