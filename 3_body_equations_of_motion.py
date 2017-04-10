# -*- coding: utf-8 -*-
"""
Created on Sun Apr  9 19:05:08 2017

@author: Jacob
"""

from __future__ import division,print_function  
from numpy import linspace,meshgrid,gradient,sqrt, array, arange
from pylab import plot, show, xlabel, ylabel
from math import pi
from scipy import interpolate
from numpy.fft import rfft, irfft


m1= 5.972e24 
m2= 7.347e22
miu=m2/(m1+m2)
N=3000

#define function for effective potential as seen in literature
def effpot(x,y):
    P1=-miu
    P2=1-miu
    r1=sqrt((x-P1)**2+y**2) 
    r2=sqrt((x-P2)**2+y**2)
    V=-(1-miu)/r1-miu/r2
    return V-(x**2+y**2)/2

#define partial differential equation
def f(r,t):
    x = r[0]
    y = r[1]
    vx = r[2]
    vy = r[3]
    xprime= vx
    yprime= vy
    vxprime= -f1(x,y)+2*vy
    vyprime= -f2(x,y)-2*vx
    return array([xprime,yprime,vxprime,vyprime], float)
    
#define forumula for conserved energy
def E(r):
    return 0.5*(r[2]**2+r[3]**2)+f0(r[0],r[1])
    
#define grid, functions for Effective potential and gradient of effective potential
X = linspace(-1.5, 1.5, N)
Y = linspace(-1.5, 1.5, N)
[x, y] = meshgrid(X, Y, sparse=True)
Z = effpot(x,y)
delz=gradient(Z)
dV_dx=delz[0]
dV_dy=delz[1]
f0= interpolate.interp2d(x,y,Z, kind='cubic')
f1= interpolate.interp2d(x,y,dV_dx, kind='cubic')
f2= interpolate.interp2d(x,y,dV_dx, kind='cubic')

#use RK4 solver and test energy conservation
a = 0.0
b = 50000
M = 100000
h = (b-a)/M

tpoints = arange(a,b,h)   
xpoints = []
ypoints = []
vxpoints = []
vypoints = []
Epoints = []  

r = array([0.2,0.7, 0.6, -0.4],float)
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

xlabel("t s")
ylabel("E J")
plot(tpoints,Epoints)
plot(tpoints,ypoints)
plot(tpoints,xpoints)
show()



