# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 12:16:14 2017

@author: Jacob
"""

from __future__ import division,print_function  
from numpy import linspace,meshgrid,sqrt, array, arange, sin, cos
from pylab import plot, show, xlabel, ylabel
from math import pi
from numpy.linalg import norm

m_earth= 5.972e24 
m_moon= 7.347e22
m_sun= 1.989e30
d_earth_sun=149.9e9
d_earth_moon=384.4e6
omegas = 0.925195985520347

def miu(mi): #normalization function
    return mi/(m_earth+m_moon) 

def distance(x0,y0,x1,y1): #distance function
    return sqrt((x1-x0)**2+(y1-y0)**2)

def effpot(theta_sun, x, y):
    x_earth=-miu(m_moon)
    y_earth=0
    x_moon=1-miu(m_moon)
    y_moon= 0
    x_sun=d_earth_sun/d_earth_moon*cos(theta_sun)
    y_sun=d_earth_sun/d_earth_moon*sin(theta_sun) 
    r_earth=distance(x_earth,y_earth,x,y)
    r_moon=distance(x_moon,y_moon,x,y)
    r_sun=distance(x_sun,y_sun,x,y)
    U = (x**2+y**2)/2+miu(m_earth)/r_earth+miu(m_moon)/r_moon+miu(m_sun)/r_sun
    return U

def partialV(r,theta_sun):#gradient of effective potential using central difference theorem
    x=r[0]
    y=r[1]
    h=0.00000001
    dV_dx= (effpot(theta_sun, x+0.5*h, y)-effpot(theta_sun, x-0.5*h, y))/h
    dV_dy= (effpot(theta_sun, x, y+0.5*h)-effpot(theta_sun, x, y-0.5*h))/h
    return array([dV_dx,dV_dy], float)
    
def r_3b(theta_sun): #position vector ofr m3
    return array([d_earth_sun/d_earth_moon*cos(theta_sun), d_earth_sun/d_earth_moon*sin(theta_sun), float])
    
def I(theta_sun):
    r_x=r_3b(theta_sun)[0]
    r_y=r_3b(theta_sun)[1]
    I_x= -miu(m_sun)*r_x/distance(r_x, r_y, 0, 0)**3
    I_y= -miu(m_sun)*r_y/distance(r_x, r_y, 0, 0)**3
    return array([I_x, I_y], float)    #indirect acceleration due to m3 as seen in literature

def f(r, theta_sun):
    x=r[0]
    y=r[1]    
    vx=r[2]
    vy=r[3]
    xprime=vx
    yprime=vy
    vxprime= partialV(r,(1-omegas)*t)[0]+I((1-omegas)*t)[0]+2*yprime
    vyprime= partialV(r,(1-omegas)*t)[1]+I((1-omegas)*t)[1]-2*xprime
    return array([xprime,yprime,vxprime,vyprime], float)

def RK4(r,t): #returns change in r as calculated by RK4
    k1 = h*f(r,(1-omegas)*t)
    k2 = h*f(r+0.5*k1,(1-omegas)*(t+0.5*h))
    k3 = h*f(r+0.5*k2,(1-omegas)*(t+0.5*h))
    k4 = h*f(r+k3,(1-omegas)*(t+h))
    r += (k1+2*k2+2*k3+k4)/6
    return r

def E(r, theta_sun):
    x=r[0]
    y=r[1]
    return 0.5*(r[2]**2+r[3]**2)-effpot(theta_sun, x, y)

a = 0.0
b = 100
N = 100000
h = (b-a)/N

tpoints = arange(a,b,h)   
xpoints = []
ypoints = []
vxpoints = []
vypoints = []
Epoints = []  

r = array([0.2, -0.6 , 0, -0],float)
#print(RK4(r,0))
for t in tpoints:
    xpoints.append(r[0])
    ypoints.append(r[1])
    vxpoints.append(r[2])
    vypoints.append(r[3])
    Epoints.append(E(r, (1-omegas)*t))    
    r = RK4(r,t)
    
plot(tpoints,Epoints)
show()

plot(tpoints, xpoints)
show()

plot(tpoints, ypoints)
show()

plot(xpoints, ypoints)
show()
