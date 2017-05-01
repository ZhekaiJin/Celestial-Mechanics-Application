from __future__ import division,print_function  
from numpy import linspace,meshgrid,sqrt, array, arange
from pylab import plot, show, xlabel, ylabel
from math import pi,log


m1= 5.972e24 
m2= 7.347e22
miu=m2/(m1+m2)
c=2.66

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
    h=0.0000001
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
    
    
#use RK4 solver and test energy conservation

b = 500
N = 1000
H = b/(N)

x_3=0.19999999996317003
y_3=0.69999999987914074

xpoints = []
ypoints = []


r = array([0.2,0.7, 0.0, 0.0],float)

def RK4(r,h,t):
    #C=c**(-log((H/h), 2))
    C=1
    R=array([r[0],r[1],r[2],r[3]],float)
    while t< 3.1*h:
        if t ==3*h:
            print("\nfor h=",h,"error x =",(x_3-R[0])*C, "error y =", (y_3-R[1])*C)
        k1 = h*f(R,t)
        k2 = h*f(R+0.5*k1, t+0.5*h)
        k3 = h*f(R+0.5*k2, t+0.5*h)
        k4 = h*f(R+k3, t+h)
        R += (k1+2*k2+2*k3+k4)/6
        t+=h
    

RK4(r,H,0)
RK4(r,H/2,0)
RK4(r,H/4,0)
RK4(r,H/8,0)




    






