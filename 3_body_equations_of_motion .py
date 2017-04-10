# -*- coding: utf-8 -*-
"""
Created on Sun Apr  9 19:05:08 2017

@author: Jacob
"""

from __future__ import division,print_function  
from numpy import linspace,meshgrid,sqrt, array, arange
from pylab import plot, show, xlabel, ylabel
from math import pi


m1= 5.972e24 
m2= 7.347e22
miu=m2/(m1+m2)

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
def f(r,t):
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
    
#use RK4 solver and test energy conservation
a = 0.0
b = 500
N = 100000
h = (b-a)/N

tpoints = arange(a,b,h)   
xpoints = []
ypoints = []
vxpoints = []
vypoints = []
Epoints = []  

r = array([0.2,0.7, 0.0, 0.0],float)
for t in tpoints:
    xpoints.append(r[0])
    ypoints.append(r[1])
    vxpoints.append(r[2])
    vypoints.append(r[3])
    Epoints.append(E(r))
    k1 = h*f(r,t)
    k2 = h*f(r+0.5*k1, t+0.5*h)
    k3 = h*f(r+0.5*k2, t+0.5*h)
    k4 = h*f(r+k3, t+h)
    r += (k1+2*k2+2*k3+k4)/6
    if t>8.5 and t<10.5:
        print(tpoints[int(t*N/b)], xpoints[int(t*N/b)], ypoints[int(t*N/b)], Epoints[int(t*N/b)])



xlabel("t s")
ylabel("E J")
plot(tpoints,Epoints)
show()

plot(tpoints, xpoints)
show()

plot(tpoints, ypoints)
show()

plot(xpoints, ypoints)
show()




