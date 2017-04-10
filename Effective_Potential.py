# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 16:11:09 2017

@author: Jacob
"""

from __future__ import print_function, division
from numpy import linspace, zeros
from pylab import plot, show, xlabel, ylabel, scatter, imshow



m1=1.989e30
m2=1.898e27
u=m2/(m1+m2)
r=1
omega=1
rm1=[1-u,0]
rm2=[-u,0]
N=1000



def r1(x,y):
    return ((x-1+u)**2+y**2)**0.5

def r2(x,y):
    return ((x+u)**2+y**2)**0.5

def V(x,y):
    return -(1-u)/r1(x,y)-u/r2(x,y)
    
def effpot(x,y):
    return V(x,y)-(x**2+y**2)/2

E=zeros((N,N), float)
xgrid=linspace(-1.5,1.5,N)
ygrid=linspace(-1.5,1.5,N)

for i in range(N):
    for j in range(N):
        if effpot(xgrid[i],ygrid[j])<=0.0:
            if effpot(xgrid[i],ygrid[j])<=-5.0:
                E[i,j]=0.0
            else:
                E[i,j]=effpot(xgrid[i],ygrid[j])
        else:
            continue
        
#print(E)
imshow(abs(E))