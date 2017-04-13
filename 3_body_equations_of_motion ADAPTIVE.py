#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 12:53:11 2017



@author: scott
"""



from __future__ import division,print_function  
from numpy import linspace,meshgrid,sqrt,array,arange
from pylab import plot, show, xlabel, ylabel, scatter
from math import pi
import time 
start_time = time.time()  #clock the start time

m1= 5.972e24 
m2= 7.347e22
miu=m2/(m1+m2)
Target=0.000001  ## change target accuray !!!!

#define function for effective potential as seen in literature
def effpot(x,y):
    P1=-miu
    P2=1-miu
    r1=sqrt((x-P1)**2+y**2) 
    r2=sqrt((x-P2)**2+y**2)
    V=-(1-miu)/r1-miu/r2 
    return V-(x**2+y**2)/2

#define partials for effpot using central difference theorem
def partialV(x,y):
    h=0.001
    dV_dx=(effpot(x+0.5*h,y)-effpot(x-0.5*h,y))/h
    dV_dy=(effpot(x,y+0.5*h)-effpot(x,y-0.5*h))/h
    return array([dV_dx,dV_dy], float)

#define partial differential equation
def f(r):
    x = r[0]
    y = r[1]
    vx = r[2]
    vy = r[3]
    xprime= vx
    yprime= vy
    vxprime= -partialV(x,y)[0]+2*vy
    vyprime= -partialV(x,y)[1]-2*vx
    return array([xprime,yprime,vxprime,vyprime], float)
    
    
#define forumula for conserved energy
def E(r):
    return 0.5*(r[2]**2+r[3]**2)+effpot(r[0],r[1])
    
def RK4(r,h):   #define Rk4    
    k1 = h*f(r)
    k2 = h*f(r+0.5*k1)
    k3 = h*f(r+0.5*k2)
    k4 = h*f(r+k3)
    return r+(k1+2*k2+2*k3+k4)/6

def Adaptive(r,h):   #define how to fine the pho with return the first approxmiation
    r1=RK4(r,h)
    R1=RK4(r1,h)
    R2=RK4(r,2*h)
    deltax=(R1[0]-R2[0])/30  #x1=R1[0],x2=R2[0],y1=R1[1],y2=R2[1]
    deltay=(R1[1]-R2[1])/30
    pho=h*Target/sqrt(deltax**2+deltay**2)
    return pho,R1
    
t,b=0,500   #change b here !!!
N = 100000
h = (b-t)/N
x,y=[],[]
tpoints,Epoints = [],[]  
r=array([0.2,0.7, 0.0, 0.0])   #change the inital condition maybe 
while t<b:                          #iterate with t and keep lower the step if pho>1
    pho,R1=Adaptive(r,h)
    if pho>1:
        tpoints.append(t)
        x.append(R1[0])  # the approxmiation using two steps will be used 
        y.append(R1[1])
        Epoints.append(E(r))
        
        t+=2*h
        r=R1
    h=h*pho**(1/4)    
#plot(x,y)

plot(tpoints,Epoints)
show()

plot(tpoints, x)
show()

plot(tpoints, y)
show()

plot(x, y)
show()

#show()
print("--- %s seconds ---" % (time.time() - start_time)) #print the time
    
    
    