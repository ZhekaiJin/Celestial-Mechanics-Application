#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 19:54:49 2017

@author: scott
"""

from __future__ import division,print_function  
from numpy import linspace,meshgrid,sqrt, array, arange, greater, less
from pylab import plot, show, xlabel, ylabel,scatter,xlim,ylim
from math import pi
from scipy.signal import argrelextrema



m1= 5.972e24 
m2= 7.347e22
miu=m2/(m1+m2)
#define h
a = 0.0
b = 500
N = 100000
h = (b-a)/N

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
    return dV_dx
    

def partialV2(x,y):
    h=0.001
    dV_dy=(effpot(x,y+0.5*h)-effpot(x,y-0.5*h))/h
    return dV_dy

'''
    
    def function(r):    #define the function
    y=(effpot(x+0.5*h,y)-effpot(x-0.5*h,y))/h
    return y
    
    def Prime(r):      #define the gradient
    xPrime=(function(r+h/2)-function(r-h/2))/h
    return xPrime
    
    def Improve(x):   #define how get the next x
    xNext=x-function(x)/Prime(x)
    return xNext
    
    def L_point(r):   #compute Lagrange point until target accuracy
    for i in range(100):
    if abs(function(r)/Prime(r))<1e-4:
    print("iteration number=",i+1)
    print("final value=",r,"m")
    break;
    r=Improve(r)
    
    L_point(0)
    
'''
    
Lagrange_point=[]    
pxpoints = []
pypoints = []
xpoints=arange(-2,2,h)
for i in xpoints :
    pxpoints.append(effpot(i,0))
    
pxpoints=array(pxpoints,float)   
A=argrelextrema(pxpoints, greater)
Cx=h*A[0]-2# Lagrage coordinates
for i in arange(len(Cx)) :
    print([Cx[i],0])
    Lagrange_point.append([Cx[i],0])

ypoints=arange(-2,2,h)
for i in ypoints :
    pypoints.append(effpot(Cx[1],i))
pypoints=array(pypoints,float)   
B=argrelextrema(pypoints, greater)
Cy=h*B[0]-2# Lagrage coordinates
for i in arange(len(Cy)) :
    print([Cx[1],Cy[i]])
    Lagrange_point.append([Cx[1],Cy[i]])
    
zip(*Lagrange_point)
scatter(*zip(*Lagrange_point))
xlim(-1.5,1.5)
ylim(-1.5,1.5)
show()



    
   
